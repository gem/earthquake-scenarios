#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cycler


def matplotlib_style():
    # Desired styling for matplotlib
    colors = cycler('color',["44aa98","ab4498","332389","86ccec","ddcc76","cd6477","882255", "117732"])
    plt.rcParams['figure.figsize'] = [6,4]
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['text.color'] = '212121'
    plt.rcParams['xtick.color'] = '212121'
    plt.rcParams['ytick.color'] = '212121'
    plt.rcParams['font.family'] = 'sans serif'
    plt.rcParams['axes.facecolor'] = 'None'
    plt.rcParams['axes.edgecolor'] = 'dimgray'
    plt.rcParams['axes.grid'] = False
    plt.rcParams['axes.grid'] = False
    plt.rcParams['grid.color'] = 'lightgray'
    plt.rcParams['grid.linestyle'] = 'dashed'
    plt.rcParams['xtick.labelsize'] = 'small'
    plt.rcParams['ytick.labelsize'] = 'small'
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.framealpha'] = 0.8
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['legend.edgecolor'] = 'None'
    plt.rcParams['legend.fontsize'] = 'medium'
    plt.rcParams['axes.labelsize'] = 'small'
    plt.rcParams['savefig.facecolor'] = 'None'
    plt.rcParams['savefig.edgecolor'] = 'None'
    plt.rc('axes', prop_cycle=colors)
    
    return


def gmd_scale():
    # Color scale for ploting ground motion values
    cmap = mpl.cm.Spectral_r
    bounds = [0.00, 0.01, 0.02, 0.03, 0.05, 0.075, 0.10, 0.20, 0.3, 0.50, 1.00]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    return cmap, norm


def grid_spacing(corners, region_crs, epicenter):
    '''
    Generate a grid with regular mesh by defining rectangular poligons
    with uniform spacing with respect to a point (epicenter).
    Grid parameters in km. 

    Parameters
    ----------
    corners: list of tuples with: (x_distance, y_distance, grid_spacing) in km.
        for example: `corners = [(100, 100, 10), (200, 200, 25)]`

    epicenter: GeoDataframe
        Expicentral coordinates for a 

    Returns
    -------
    DataFrame with grided points (Point as geometry objects) in EPSG:4326.
    '''
    gdf = gpd.GeoDataFrame()
    df = gpd.GeoDataFrame()

    for i, (x,y, spc) in enumerate(corners):    
        # Change distance from km to m
        x = x * 1e3
        y = y * 1e3
        spc = spc * 1e3
        
        # Create GeoDataFrame with polygons information
        d = {'polygon':[i] * 4, 
            'corner': ['p1', 'p2', 'p3', 'p4'],
            'geometry': [Point(-x, -y), Point(-x, y), Point(x, y), Point(x, -y)]}    
        g = gpd.GeoDataFrame(d, crs=region_crs)
        
        # Move polygon coordinates to centroid
        g.geometry = g.translate(xoff=epicenter.geometry.x,
                                yoff=epicenter.geometry.y)    
        gdf = pd.concat([gdf, g])
        
        # Create grid (entire polygon)
        xmin, ymin, xmax, ymax = g.total_bounds
        xcoords = [c for c in np.arange(xmin, xmax + spc, spc)] # Create x coordinates
        ycoords = [c for c in np.arange(ymin, ymax + spc, spc)] # Create y coordinates
        grid = np.array(np.meshgrid(xcoords, ycoords)).T.reshape(-1, 2) # Create all combinations of xy coordinates
        
        # Remove points in inner polygon
        if i ==0:
            outbox = grid
        else:
            inner = gdf[gdf.polygon == i -1]
            x1, y1, x2, y2 = inner.total_bounds    
            ll = np.array([x1, y1])  # lower-left
            ur = np.array([x2, y2])  # upper-right
            
            inidx = np.all(np.logical_and(ll <= grid, grid <= ur), axis=1)
            inbox = grid[inidx]
            outbox = grid[np.logical_not(inidx)]
        
        pts = gpd.GeoDataFrame(
            geometry=gpd.points_from_xy(outbox[:,0], outbox[:,1],
                                        crs=region_crs))        
        # grid in GeoDataframe
        df = pd.concat([df, pts])

        
    # Move coordinates back to 4326
    df = df.to_crs('EPSG:4326')
    df['LONGITUDE'] = df.geometry.x
    df['LATITUDE'] = df.geometry.y
    
    return df