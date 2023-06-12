#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import json
import numpy as np
import pandas as pd

import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt


def read_usgs_json(json_path):
    '''
    Read USGS stations.json file and extract stations recorded values and
    their associated uncertainty.
    '''
    
    # Read file using pandas
    with open(json_path) as f:
        sj = json.load(f)
        stations = pd.json_normalize(sj, 'features')
        stations['eventid'] = sj['metadata']['eventid']
        
    # Rename columns
    stations.columns = [col.replace('properties.','') for col in stations.columns]

    # Extract lon and lat
    stations[['lon', 'lat']] = pd.DataFrame(
        stations['geometry.coordinates'].to_list())
    

    # Get values for available IMTs (PGA and SA)
    # ==========================================
    # The "channels/amplitudes" dictionary contains the values recorded at 
    # the seismic stations. The values could report the 3 components, in such
    # cases, take the componet with maximum PGA (and in absence of PGA, the 
    # first IM reported).
      
    channels = pd.DataFrame(stations.channels.to_list())
    vals = pd.Series([], dtype = 'object')
    for row, rec_sation in channels.iterrows():
        rec_sation.dropna(inplace=True)
            
        # Iterate over different columns. Each colum can be a component
        data = []
        pgas = []
        for index, chan in rec_sation.iteritems():
            try:
                if chan["name"].endswith("Z") or chan["name"].endswith("U"):
                    continue
                # print(chan["name"])
                df = pd.DataFrame(chan["amplitudes"])
                if 'pga' in df.name.unique():
                    pga = df.loc[df['name']=='pga','value'].values[0]
                else:
                    pga = df['value'][0]
                if pga is None or pga == "null":
                    continue
                elif isinstance(pga, str):
                    pga = float(pga)
                pgas.append(pga)
                data.append(chan["amplitudes"])
   
            except TypeError:
                print('boh')
        
        # get values for maximum component
        if pgas:
            max_componet = pgas.index(max(pgas))
            vals[row] = data[max_componet]
        else:
            vals[row] = None
            
            
    # The "pgm_from_mmi" dictionary contains the values estimated from MMI.
    # Combine both dictionaries to extract the values. 
    # They are generally mutually exclusive (if mixed, the priority is given  
    # to the station recorded data). 
    
    try:
        # Some events might not have macroseismic data, then skip them
        vals = vals.combine_first(stations['pgm_from_mmi']).apply(pd.Series)
    except Exception as e:
            print(e, 'not available in json')
            vals = vals.apply(pd.Series)
    
    # Arrange columns since the data can include mixed positions for the IMTs
    values = pd.DataFrame()
    for col in vals.columns:
        df = vals[col].apply(pd.Series)
        df.set_index(['name'], append=True, inplace=True)
        df.drop(columns=['flag', 'units'], inplace=True)
        if 0 in df.columns:
            df.drop(columns=[0], inplace=True)
        df = df.unstack('name')
        df.dropna(axis=1, how='all', inplace=True)
        df.columns = [col[1]+'_'+col[0] for col in df.columns.values]
        
        for col in df.columns:
            if col in values:
                # Colum already exist. Combine values in unique column
                values[col] = values[col].combine_first(df[col])
            else:
                values = pd.concat([values, df[col]], axis=1)
    values.sort_index(axis=1, inplace=True)
    
    # Add recording to main DataFrame
    stations = pd.concat([stations, values], axis=1)
    
    return stations


def json_to_ecd(stations):
    '''
    Adjust USGS format to match the ECD (Earthquake Consequence Database)
    format
    
    '''
    
    # Adjust column names to match format
    stations.columns = stations.columns.str.upper()
    stations.rename(columns={
        'CODE': 'STATION_ID',
        'NAME': 'STATION_NAME',
        'LON': 'LONGITUDE', 
        'LAT': 'LATITUDE',
        'INTENSITY': 'MMI_VALUE',
        'INTENSITY_STDDEV': 'MMI_STDDEV',
        }, inplace=True)
    
    # Identify columns for IMTs:
    imts = []
    for col in stations.columns:
        if 'DISTANCE_STDDEV' == col:
            continue
        elif '_VALUE' in col or '_LN_SIGMA' in col or '_STDDEV' in col:
           imts.append(col)
    
    # Identify relevant columns
    cols = ['STATION_ID', 'STATION_NAME', 'LONGITUDE', 'LATITUDE', 
            'STATION_TYPE', 'VS30'] + imts
    df = stations[cols].copy()
    
    # Add missing columns
    df.loc[:, 'VS30_TYPE'] = 'inferred'
    df.loc[:, 'REFERENCES']= 'Stations_USGS'

    # Adjust PGA and SA untis to [g]. USGS uses [% g]
    adj_cols = [item for item in imts 
                if '_VALUE' in item and 
                'PGV' not in item and 
                'MMI' not in item]
    df.loc[:, adj_cols] = round(df.loc[:, adj_cols].
                                apply(pd.to_numeric, errors='coerce') / 100, 6)
    
    return df
