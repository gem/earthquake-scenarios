#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt

import utils
from openquake.commonlib.datastore import read

# Get common matplotlib style and color bar
utils.matplotlib_style()
CMAP, NORM = utils.gmd_scale()

def oq_get_gmfs(calc_id):
    '''
    Get DataFrame for gmfs
    '''    
    # Read dstore
    dstore = read(calc_id)
    oq = dstore["oqparam"]
    description = oq.description
    
    sites = dstore.read_df('sitecol').rename(columns={'sids':'sid'})
    gmf_data = dstore.read_df('gmf_data')
    df = pd.merge(sites[['sid', 'custom_site_id', 'lon', 'lat']], 
                  gmf_data, 
                  how='right', on='sid')

    # read IMTs
    imts = list(oq.imtls)
    for x,im in enumerate(imts):
        df.rename(columns={f'gmv_{x}':im}, inplace=True)
    
    # Get GMPEs
    events = dstore.read_df('events').rename(columns={'id':'eid'})
    full_lt = dstore['full_lt']
    trt = (dstore
                .read_df('ruptures')
                .loc[:, ['id', 'trt_smr']]
                .rename(columns={'id':'rup_id'})
                )
    trt['trti'] = trt.trt_smr // len(full_lt.sm_rlzs)
    events = events.merge(trt, on='rup_id')   
    events['gmpe'] = ''
    for rlz in events.rlz_id:
        trti = events.loc[events.rlz_id == rlz, 'trti'].values[0]
        gsim = str(full_lt.get_realizations()[rlz].gsim_rlz.value[trti])
        # Adjust gsim name
        gsim = gsim.replace('[', '').replace(']', '')
        if 'ModifiableGMPE' in gsim:
            gsim = gsim[gsim.find('.') + 1 : gsim.find(' = {}')]
        # Add gmpe to events DataFrame
        events.loc[events.rlz_id == rlz, 'gmpe'] = gsim
    
    df_gmf = pd.merge(events[['eid', 'rlz_id', 'gmpe']],
                      df,
                      on='eid',
                      how='outer',
                      )

    return df_gmf, description


def write_gmf_csv(df, imt, comment=None, out_path=None, suffix=None):
    '''
    Write ground motion fields in csv.

    Parameters
    ----------
    df : DataFrame
        Ground motion fields. It should include the columns for:
            ['lon', 'lat', 'gmpe'] plus the columns for each imt.
    imt : str
        Intensity to be saved. E.g. 'PGA'
    comment : str
        Include a commented line at the beginning of the file
    out_path : str, optional
        Folder path to save the figure. The default is None (not saved).
    suffix : str or float, optional
        Add suffix at the end of the image file name when saving it.

    Returns
    -------
    df : pd.DataFrame

    '''

    # Reshape data
    df = df.set_index(['custom_site_id','lon','lat','gmpe'])[imt].unstack().reset_index().copy()

    # Save CSV
    if out_path:
        if suffix:
            file_name = f'gmf_median_{imt}_{str(suffix)}.csv'
        else:
            file_name = f'gmf_mediann_{imt}.csv'
        file_path = os.path.join(out_path, file_name)
        with open(file_path, 'w') as f:
            if comment:
                f.write(f'# {comment}\n')  # Write comment line 
            df.to_csv(f, index=False)
        print(f'File saved to {file_path}')

    return df


def read_log(log):
    '''
    Function to extract key information from OQ log file.
    The log file follows the ECD format
    '''
    
    lines = open(log, 'r').readlines()

    # Get calculation details
    calc_id = int(lines[0][8:-1])
    description = lines[1][17:]
    rs, gmlt, rup = description.split(',')[1:]
    rs = rs.replace('Stations:', '')
    gmlt = gmlt.replace('gmlt:', '')
    rup = rup.replace('Rupture:', '').replace('\n', '')

    # Get time
    try:
        time = [line for line in lines if 'oqdata/calc_' in line][0]
        time = int(time[time.find(' in ') + 4: -8].strip())
    except Exception as e: 
        # If no time is found, then the calculation has an error
        raise Exception(f"Calculation with error. Check log file: {log}")

    # Create DataFrame
    cols=['calc_id', 'description', 'cal_time', 
          'recording_stations', 'gmlt', 'rupture', 'gmpe', 'imt', 
          'nominal_bias_mean', 'nominal_bias_stdev']
    calc = []

    # Get bias
    bias = [line for line in lines if 'Nominal bias' in line]
    if bias:
        # Calculation with station data
        for line in bias:
            ini = line.find('INFO]')
            if ini != -1:
                line = line[ini + 6 :] # Remove info from initial paragraph                
            gmpe = line.split(':')[1].split(',')[0].strip(' [] ') 
            imt = line.split(':')[2].split(',')[0].strip()
            bias_mean = float(line.split(':')[3].split(",")[0].replace('\n', '').strip())
            bias_stdv = float(line.split(':')[4].replace('\n', '').strip())
            vals = [calc_id, description, time, rs, gmlt, rup, gmpe, imt, bias_mean, bias_stdv]
            data = pd.DataFrame(dict(zip(cols, vals)), index=[0])
            calc.append(data)
    else:
        # Calculation without station data
        gmpe = ''
        imt = ''
        bias_mean = np.nan
        bias_stdv = np.nan
        vals = [calc_id, description, time, rs, gmlt, rup, gmpe, imt, bias_mean, bias_stdv]
        data = pd.DataFrame(dict(zip(cols, vals)), index=[0])
        calc.append(data)
        
    df = pd.concat(calc, ignore_index=True)

    assert df.shape[0]>0, f'No data extracted from log file {log}'

    return df, calc_id


def plot_df(df, pad=None, **kwargs):
    '''
    Plot ground motion fields starting from a given DataFrame.

    Parameters
    ----------
    df : DataFrame
        It must have columns for ['lon', 'lat']
    
    pad : float
        Padding around the geometry of the figure. Default None.

    Returns
    -------
    fig : matplotlib.figure
        https://matplotlib.org/stable/api/figure_api.html
    ax : matplotlib.axes
        https://matplotlib.org/stable/api/axes_api.html

    '''

    # Create GeoDataFrame in WGS84
    gdf = gpd.GeoDataFrame(df,
                           geometry=gpd.points_from_xy(df.lon, df.lat),
                           crs='EPSG:4326')    
    
    # Get corner values for figure
    xmin, ymin, xmax, ymax = gdf.total_bounds
        
    # Plot values
    fig, ax = plt.subplots(figsize=(12,8)) # , alpha=0.5) # alpha not supported in OQ libraries
    ax.set_aspect('equal')
            
    gdf.plot(ax=ax,
             cmap=CMAP,
             norm=NORM,
             **kwargs,
            )

    # Include legend
    ax.legend(edgecolor='lightgrey')
    
    # Adjust plot limits
    if pad:
        ax.set_xlim(xmin-pad, xmax+pad)
        ax.set_ylim(ymin-pad, ymax+pad)

    # Add default basemap: Stamen Terrain (uses Web Mercator --> epsg=3857)
    # Additional basemaps available at:
    # https://contextily.readthedocs.io/en/latest/providers_deepdive.html#What-is-this-%E2%80%9Cprovider%E2%80%9D-object-?
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron,
                    crs=gdf.crs, alpha=0.8)            

    return fig, ax


def plot_stations(fig, ax, folder, description):
    '''
    Append to a plot (fig, ax) the stations
    
    Parameters
    -----------
    folder: str
        Folder with station files
    
    description: string to identify the station file to plot
    '''
    # Include stations if available
    if 'Stations:Seismic' in description:
        stations_file = os.path.join(folder, 'stationlist_seismic.csv')
    elif 'Stations:All' in description:
        stations_file = os.path.join(folder, 'stationlist_all.csv')
    elif 'Stations:None' in description:
        stations_file = None
    else:
        raise AssertionError('Stations not found in [None, Seismic, All]') 
    
    if stations_file:
        df_stations = pd.read_csv(stations_file)
        imt = 'PGA'
        df_stations.rename(columns={'LONGITUDE':'lon', 
                                    'LATITUDE':'lat', 
                                    'PGA_VALUE': 'PGA'}, inplace=True)
        gdf_rs = gpd.GeoDataFrame(df_stations,
                                  geometry=gpd.points_from_xy(
                                  df_stations.lon, df_stations.lat),
                                  crs='EPSG:4326')

        # Plot seismic stations
        dfs = gdf_rs.loc[gdf_rs.STATION_TYPE == 'seismic']
        if len(dfs) >= 1:
            dfs.plot(ax=ax,
                        column=imt,
                        alpha=0.6,
                        marker='^', 
                        markersize=100,
                        cmap=CMAP,
                        norm=NORM,
                        edgecolor='grey', 
                        linewidth=0.5,
                        label='seismic',
                        )
        # Plot macroseismic stations
        dfm = gdf_rs.loc[gdf_rs.STATION_TYPE == 'macroseismic']
        if len(dfm) >= 1:
            dfm.plot(ax=ax,
                        column=imt,
                        alpha=0.6,
                        marker='o', 
                        markersize=50,
                        cmap=CMAP,
                        norm=NORM,
                        edgecolor='grey', 
                        linewidth=0.5,
                        label='macroseismic',
                        )
        # Include legend for stations
        ax.legend(edgecolor='lightgrey')

    return fig, ax

def get_imfd(df_log, gmfs):
    '''
    Calculate the Intensity Measure Frequency Distribution (IMFD) curves
    '''

    # Ground motion values (gmvs) to use as reference
    gmvs = [0.05, 0.75, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 1, 1.5]

    # Count the number of sites that exceed each IM threshold for each column
    imfd = pd.DataFrame({gmv: (gmfs.iloc[:, 3:] >= gmv).sum() for gmv in gmvs})
    # imfd = imfd.reset_index().rename(columns={'index':'gmpe'})
    df = imfd.stack().reset_index()
    df.columns = ['gmpe', 'PGA', 'Number']

    # Add columns with calculation data
    cols = ['rupture', 'recording_stations', 'description', 'calc_id']
    for col in cols:
        df.insert(0, col, df_log.loc[0, col])
    
    return df