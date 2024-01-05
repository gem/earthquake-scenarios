#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from openquake.commonlib.oqvalidation import OqParam
from openquake.commonlib.readinput import get_rupture


def repture_xml_to_df(filepath, add_geometry=False):
    '''
    Parameters
    ----------
    filepath : str, file path with OQ rupture format

    Returns
    -------
    rup : OQ hazardlib rupture object
        DESCRIPTION.
    df : DataFrame with rupture parameters

    '''
    
    # Read xml rupture as hazardlib object
    oqp = OqParam(calculation_mode='scenario')
    oqp.inputs['rupture_model'] = filepath
    rup = get_rupture(oqp)

    # Attributs of interest
    hyp_attrs = ['longitude', 'latitude', 'depth']
    surface_attrs = ['strike', 'dip']
    base_attrs = ['rake', 'mag']

    rup_df = {}
    for attr in surface_attrs:
        try:
            rup_df[attr] = rup.surface.__getattribute__(attr)
        except AttributeError as error:
            print(f'Skipping attribute in {filepath}:\n', error)
    for attr in hyp_attrs:
        rup_df[attr] = rup.hypocenter.__getattribute__(attr)
    
    for attr in base_attrs:
        rup_df[attr] = rup.__getattribute__(attr)

    # Convert to DataFrame
    df = pd.DataFrame(rup_df, index=[0])

    if add_geometry:
        # Include rupture 3D geometry
        boundaries = rup.surface.get_surface_boundaries_3d()    
        coords = [[boundaries[0][i], 
                boundaries[1][i], 
                boundaries[2][i]] for i in range(len(boundaries[0]))]
        wkt_polygon_z = f'POLYGON(({",".join(" ".join(str(x) for x in c) for c in coords)}))'
        # gdf = gpd.GeoDataFrame(df, geometry=[wkt_polygon_z], crs='EPSG:4326')
        df['geometry'] = wkt_polygon_z

    return rup, df    


