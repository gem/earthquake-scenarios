#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import xml.etree.ElementTree as ET

import utils


def gdf_epicentre(file_path):
    # Epicenter as GeoDataFrame
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = root.tag[1:-5]
    lon, lat = None, None
    
    for child in root.iter():
        if child.tag == r"{" + namespace + r"}hypocenter":
            lon, lat = float(child.attrib['lon']), float(child.attrib['lat'])
    epicenter = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon], [lat]),
                                 crs='EPSG:4326')
    
    return epicenter


def stations_plot(df, value='PGA_VALUE', title=None, 
                  legend_orientation='horizontal'):
    # Get common matplotlib style
    utils.matplotlib_style()
    cmap, norm = utils.gmd_scale()
    
    # Create GeoDataFrame with WGS84 and PGA values
    df_plot = df[['LONGITUDE', 'LATITUDE', 'PGA_VALUE', 'STATION_TYPE']].copy()
    
    gdf = gpd.GeoDataFrame(df_plot,
                           geometry=gpd.points_from_xy(df_plot.LONGITUDE, 
                                                       df_plot.LATITUDE),
                           crs='EPSG:4326')
    
    # Plot stations PGA (g) value
    fig, ax = plt.subplots(figsize=(12, 8)) # , alpha=0.5) # alpha not supported in OQ libraries
    ax.set_aspect('equal')
    
    idx = gdf.STATION_TYPE == 'seismic'
    
    seismic = gdf[idx]
    macroseismic = gdf[~idx]
    
    if len(seismic) != 0:
        seismic.plot(ax=ax,
                     column=value,
                     alpha=0.8,
                     marker='^', 
                     markersize=100,
                     cmap=cmap,
                     norm=norm,
                     edgecolor='lightgrey', 
                     linewidth=0.5,
                     label=f'Seismic stations [{len(seismic)}]')
    
    
    if len(macroseismic) != 0:
        macroseismic.plot(ax=ax,
                          column=value,
                          alpha=0.8,
                          marker='o', 
                          markersize=80,
                          cmap=cmap,
                          norm=norm,
                          edgecolor='lightgrey', 
                          linewidth=0.5,
                          label=f'Macroseismic stations [{(~idx).sum()}]')
        
    # Add default basemap: Stamen Terrain (uses Web Mercator --> epsg=3857)
    # Additional basemaps available at:
    # https://contextily.readthedocs.io/en/latest/providers_deepdive.html#What-is-this-%E2%80%9Cprovider%E2%80%9D-object-?
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron,
                    crs=gdf.crs, alpha=0.8)
    
    # Add legend for stations
    ax.legend(loc='lower left')
    
    # Add colormap in figure
    fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap),
                 label='PGA [g]', pad=0.05,shrink=0.75,
                 orientation=legend_orientation)
    
    if title:
        ax.set_title(title, fontsize=14)
    
    return fig, ax