#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from openquake.commands.prepare_site_model import main as oq_site_model


def add_vs30_from_ref(df, vs30_path, ref='USGS'):
    '''
    Find the closest Vs30 value from values in `vs30_path` to the pass
    DataFrame.

    Parameters
    ----------
    df : DataFrame with coordinates ['LONGITUDE', 'LATITUDE'].
         Can include a `VS30` column, which can have specific values.

    vs30_path : str.
        Path to file with reference vs30 values following OQ format.
        (e.g., USGS in hdf5)

    Returns
    -------
    DataFrame with updated VS30 column if empty values, plus columns for 
    reference data (`VS30_ref`)

    '''
    # Round coordinates for OQ compatibility
    df = df.round(6)
    df.columns = df.columns.str.upper()
    
    # Columns to find unique sites
    coord = ['LONGITUDE', 'LATITUDE']
    
    # Get unique sites
    sites = df[coord].drop_duplicates()
    sites.columns = ['lon','lat']
        
    # Use OQ to prepare_site_model
    print(f'Including VS30 from {ref} for {len(sites)} sites')    
    site_model = oq_site_model( vs30_path,
                                sites_csv=sites,
                                output=None)
    
    # Round coordinates for OQ compatibility
    site_model = pd.DataFrame(site_model.array).round(6)
    
    # Add VS30 data to DataFrame
    site_model.columns = site_model.columns.str.upper()
    site_model.rename(columns={'LON': 'LONGITUDE',
                               'LAT': 'LATITUDE',
                               'VS30': f'VS30_{ref}'},
                      inplace=True)

    # Drop reference VS30 if already in df
    if f'VS30_{ref}' in df.columns:
        df.drop(columns=f'VS30_{ref}', inplace=True)

    df = df.merge(site_model[coord + [f'VS30_{ref}']],
                  how='left',
                  on=coord)
    
    if 'VS30' in df.columns:
        no_vs30 = df.VS30.isnull()
        if len(df[no_vs30]) >= 1:
            print(f'  Adding {len(df[no_vs30])} missing VS30 values from {ref}')
            df.loc[no_vs30, 'VS30'] = df.loc[no_vs30, f'VS30_{ref}']        
            if 'VS30_TYPE' in df.columns:
                df.loc[no_vs30, 'VS30_TYPE'] = f'inferred_{ref}'
        else:
            print('No values added. All rows have VS30 values')
    else:
        print(f'  Added column for `VS30_{ref}`')
        df['VS30_TYPE'] = f'inferred_{ref}'


    # Raise error if empty values in VS30 after merge
    assert df.VS30.isnull().any() == False, 'Error in getting Vs30 from USGS'
 
    
    return df

