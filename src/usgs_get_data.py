#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import time
from datetime import date
import pandas as pd

import requests
import json
import urllib.request


def query_usgs_data(usgs_id, event_path):
    format = "geojson"
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid={usgs_id}&format={format}"
    
    # Submit request
    r = requests.get(url)
    
    # Convert to json
    r_json = json.loads(r.text)
    
    # Extract relevant component
    usgs_dict = r_json['properties']['products']['shakemap'][0]['contents']
    usgs_info = dict()
    usgs_info['coordinates'] = r_json['geometry']['coordinates']
    usgs_info['mmi'] = r_json['properties']['mmi']
    usgs_info['time'] = r_json['properties']['time']

    # ECD content destination and names
    # - Recording stations
    # - Rupture data
    # - ShakeMap info: image, json information (for GMPEs) and zip    
    out_folder = os.path.join(event_path)
    ecd_paths = {
        "rupture.json": os.path.join(out_folder, "Rupture", "rupture_USGS.json"),
        "stationlist.json": os.path.join(out_folder, "Recording_Stations", "stationlist.json"),         
        "intensity.jpg": os.path.join(out_folder, "OpenQuake_gmfs", "USGS_image.jpg"),
        "info.json": os.path.join(out_folder, "OpenQuake_gmfs", "shakemap_info.json"),
        # "shape.zip": os.path.join(out_folder, "Shake_Map", "shape_USGS.zip"),
        }
    
    # Get relevant download URLs required
    usgs_urls = ecd_paths.copy()    
    for key in usgs_urls:
        print(key)
        
        if f"download/{key}" in usgs_dict.keys():
            # Set up timing for downloading data when bad connection
            retries = 1
            success = False
        else:
            success = True
            print(f"\x1b[0;31m   Could not find ShakeMap product for: {key}",
                  "\n   Check USGS ShakeMap page Downloads to confirm.",
                  f" ID: {usgs_id} \x1b[0m")

        while not success:
            try:
                # Get information irl
                usgs_urls[key] = usgs_dict[f"download/{key}"]['url']
                
                # Download data and place it in correct folder
                print(f"   Downloading {key}")
                urllib.request.urlretrieve(usgs_urls[key], ecd_paths[key])
                success = True
                print(f"   Saved in {ecd_paths[key].split(os.sep)[-1]}")
                
            except Exception as e:
                wait = retries * 20
                print("\x1b[0;31m Conection error. Trying again in 20sec\x1b[0m")
                print(e)
                sys.stdout.flush()
                time.sleep(wait)
                retries += 1
                
    usgs_info['urls'] = usgs_urls
    usgs_info['urls']['home'] = f"https://earthquake.usgs.gov/earthquakes/eventpage/{usgs_id}/executive"
    usgs_info['ecd_paths'] = ecd_paths
    return usgs_info


def roman_num(num):
    
    integer = int(round(num, 0))
    
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    mmi = dict(zip(list(range(1,10)), roman))    
    intensity = mmi[integer]
    
    return intensity


def ini_readmes(event, event_path, usgs_id, usgs_info, wiki):

    usgs_urls = usgs_info['urls']
    ecd_paths = usgs_info['ecd_paths']
    access_date = date.today().strftime("%B %Y")
    
    # Recording_Stations README
    # =======================================================================
    key = "stationlist.json"
    fpath = ecd_paths[key]
    
    rpath = fpath.replace(fpath.split(os.sep)[-1], 'README.md')
    f = open(rpath, 'r', encoding="utf-8")
    content = f.read()
    f.close

    if os.path.exists(fpath):        
        content = content.replace("{URL_STATIONS}", usgs_urls[key])
    else:
        repl = ". Raw file [`stationlist.json`]{URL_STATIONS}/shakemap/stations"
        content = content.replace(repl, " not available.")

    content = content.replace("{ACCESS_DATE}", access_date)        
    f = open(rpath, 'w', encoding="utf-8")
    f.write(content)
    f.close()    

    # Rupture README
    # =======================================================================
    key = "rupture.json"
    fpath = ecd_paths[key]
    
    rpath = fpath.replace(fpath.split(os.sep)[-1], 'README.md')
    f = open(rpath, 'r', encoding="utf-8")
    content = f.read()
    f.close

    if os.path.exists(fpath):        
        content = content.replace("{RUPTURE_URL}", usgs_urls[key])
    else:
        repl = "`USGS.json`: USGS rupture. {RUPTURE_URL}"
        content = content.replace(repl, "USGS rupture not available.")

    content = content.replace("{ACCESS_DATE}", access_date)        
    f = open(rpath, 'w', encoding="utf-8")
    f.write(content)
    f.close()
    
    # ShakeMap README
    # =======================================================================
    # key = "shape.zip"
    # fpath = ecd_paths[key]
    
    # rpath = fpath.replace(fpath.split(os.sep)[-1], 'README.md')
    # f = open(rpath, 'r', encoding="utf-8")
    # content = f.read()
    # f.close

    # if os.path.exists(fpath):        
    #     content = content.replace("{USGS_ID}", usgs_id)
    # else:
    #     repl = "`USGS_image.jpg` and `shape_USGS.zip`: USGS information. https://earthquake.usgs.gov/earthquakes/eventpage/{USGS_ID}/shakemap/intensity."
    #     content = content.replace(repl, "No USGS ShakeMaps available.")

    # content = content.replace("{ACCESS_DATE}", access_date)        
    # f = open(rpath, 'w', encoding="utf-8")
    # f.write(content)
    # f.close()

    # job.ini README
    # ======================================================================= 
    jobs = ['job_stations_none.ini', 'job_stations_seismic.ini']

    for job in jobs:
        rpath = os.path.join(event_path, 'OpenQuake_gmfs', job)
        f = open(rpath, 'r', encoding="utf-8")
        content = f.read()
        f.close

        content = content.replace("{EVENT_ID}", event.replace('DRAFT_', ''))

        f = open(rpath, 'w', encoding="utf-8")
        f.write(content)
        f.close()

    # References README - NOTE: References folder does not exist in new format
    # =======================================================================  
    # rpath = os.path.join(event_path, 'References', 'README.md')
    # f = open(rpath, 'r', encoding="utf-8")
    # content = f.read()
    # f.close

    # content = content.replace("{USGS_ID}", usgs_id)
    # content = content.replace("{WIKI}", wiki.replace(' ', '_'))

    # f = open(rpath, 'w', encoding="utf-8")
    # f.write(content)
    # f.close()


    print("READMEs updated")

    return

def get_wiki_info(query):
    
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'titles': query,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
            }
     
    response = requests.get(url, params=params)
    data = response.json()
    page = next(iter(data['query']['pages'].values()))

    if 'extract' in page.keys():
        exintro =  page['extract'].split('\n')[0]
    else:
        print(f"\x1b[0;31m   WARNING: Empty data in Wikipedia for `{query}`\x1b[0m")
        exintro="  ... TO BE ADDED ..."
        
    return exintro


def home_readme(dfe, event_path, usgs_info):
    
    mag = dfe.name.split('_')[1][1:]
    # Read referance eq information table
    path_table = os.path.join(event_path,'earthquake_information.csv')
    df = pd.read_csv(path_table, index_col='FIELD')
    
    event_date = dfe.name[:4] + '-' + dfe.name[4:6] + '-' + dfe.name[6:8]
    
    # Add earthquake info based on USGS
    df.loc['Year', 'DESCRIPTION'] = dfe.name[:4]
    df.loc['Country', 'DESCRIPTION'] = dfe.COUNTRY
    df.loc['Event_Name', 'DESCRIPTION'] = dfe.NAME
    df.loc['Local_Date', 'DESCRIPTION'] = event_date
    df.loc['Local_Time', 'DESCRIPTION'] = usgs_info['time']
    df.loc['Longitude', 'DESCRIPTION'] = usgs_info['coordinates'][0]
    df.loc['Latitude', 'DESCRIPTION'] = usgs_info['coordinates'][1]
    df.loc['Depth_(km)', 'DESCRIPTION'] = usgs_info['coordinates'][2]
    df.loc['Mw', 'DESCRIPTION'] = mag
    df.loc['Max_Intensity_(MMI)', 'DESCRIPTION'] = roman_num(usgs_info['mmi'])
    df.loc['USGS page', 'DESCRIPTION'] = usgs_info['urls']['home']

    # Get info from Wikipedia
    if len(dfe.WIKI) != 0:
        wiki_summary = get_wiki_info(dfe.WIKI)
        wiki_url = f"https://en.wikipedia.org/wiki/{dfe.WIKI}"
        wiki_url = wiki_url.replace(' ', '_')

        df.loc['Wikipedia page', 'DESCRIPTION'] = wiki_url

    # Adjust home README    
    rpath = os.path.join(event_path, 'README.md')
    f = open(rpath, 'r', encoding="utf-8")
    content = f.read()
    f.close

    table = df.to_markdown()
    content = content.replace(
        '{NAME}', dfe.NAME).replace(
        '{MAGNITUDE}', mag).replace(
        '{DATE}', event_date).replace(
        '{COUNTRY}', dfe.COUNTRY).replace(
        '{WIKI_SUMMARY}', wiki_summary).replace(
        '{WIKI_URL}', wiki_url).replace(
        '{SHAKEMAP_URL}', usgs_info['urls']['intensity.jpg']).replace(
        '{TABLE}', table)

    f = open(rpath, 'w', encoding="utf-8")
    f.write(content)
    f.close()

    # Adjust `earthquake_information.csv`
    df.to_csv(path_table)

    print("Main README generated\n")    

    return

