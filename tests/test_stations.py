# -----------------------------------------------------------------------------
#   CONFIGURATION
# -----------------------------------------------------------------------------

# Dependencies
import os
import glob
import pandas as pd
import pytest

# -----------------------------------------------------------------------------
#   INITIALIZATION
# -----------------------------------------------------------------------------

# Determine all relevant country folders
skip_folders = ['src', 'tests', 'World']

regions = sorted([folder for folder in next(os.walk('.'))[1] if folder
                not in skip_folders
                and not folder.startswith(".")])
    
events = glob.glob('**/*_M*/', recursive=True)

# Arrange DataFrame with event paths
df = pd.DataFrame({'Event_Path':events}).explode('Event_Path')
df.Event_Path = df.Event_Path.apply(lambda x: os.path.normpath(x))
df['Region'] = df.Event_Path.str.split(os.sep, expand=True)[0]
df['Country'] = df.Event_Path.str.split(os.sep, expand=True)[1]
df['Event_Folder'] = df.Event_Path.str.split(os.sep, expand=True)[2]

# Include events within a sequence
sequence = df.Event_Path.str.split(os.sep, expand=True)[3]
df.loc[sequence != '', 'Event_Folder'] = sequence[sequence != '']

# Find all individual files with recording stations
files = glob.glob(os.path.join('**', '3_Recording_Stations', 'Stations_*.csv'),
                     recursive=True)

# Ignore folders marked as DRAFT
ignore = True
if  ignore:
    draft_prefix = "DRAFT_"
    edx = df.Event_Folder.str.startswith(draft_prefix) # non-draft indices
    if edx.any():
        df = df[~edx]
    files = [x for x in files if x.find('DRAFT_') == -1]


# -----------------------------------------------------------------------------
#   CHECKS FOR `Stations_USGS.csv` FILE
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df.Event_Path)
def test_stations_files_exist(event):
    station_path = os.path.join(event, "3_Recording_Stations")
    
    if event.find('_Sequence_') == -1:
        # Check USGS files exist
        # Skip events with no USGS data
        skip_events = [
                    os.path.join('South_America', 'Colombia', '20041115_M7.2_Pizarro'),
                    os.path.join('Africa', 'Malawi', '19890310_M6.2_Salima'),
                    os.path.join('Africa', 'Malawi', '20091219_M6.0_Karonga'),
                    ]
        if not any(event in s for s in skip_events):
            # stationlist.json
            file_path = os.path.join(station_path, "stationlist.json")
            error_msg = "Required `stationlist.json` file does not exist"
            assert os.path.exists(file_path), error_msg
        
            # Stations_USGS.csv
            file_path = os.path.join(station_path, "Stations_USGS.csv")
            error_msg = "Required `Stations_USGS.csv` file does not exist"
            assert os.path.exists(file_path), error_msg

        # Check `Stations_Unique.csv` exist
        # If only one reference is available, then don't check Stations_Unique
        stations = glob.glob(os.path.join(station_path, 'Stations_*.csv'))
        if len(stations) > 1:
            file_path = os.path.join(station_path, "Stations_Unique.csv")
            error_msg = "Required `Stations_Unique.csv` file does not exist"
            assert os.path.exists(file_path), error_msg
 
        # Check `README.md` exist
        file_path = os.path.join(station_path, "README.md")
        error_msg = "Required `README.md` file does not exist"
        assert os.path.exists(file_path), error_msg
    
        # Check `recording_stations.png` exist
        file_path = os.path.join(station_path, "recording_stations.png")
        error_msg = "Required `recording_stations.png` file does not exist"
        assert os.path.exists(file_path), error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR CONTENTS IN `Stations_XXX.csv` FILE
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('file_path', files)
def test_stations_contents(file_path):
    # Get event name
    event = os.path.join(file_path.split(os.sep)[0],
                         file_path.split(os.sep)[1],
                         file_path.split(os.sep)[2])
    
    df = pd.read_csv(file_path)
    
    # Check mandatory columns
    cols = ['STATION_ID', 'STATION_NAME', 'LATITUDE', 'LONGITUDE',
            'STATION_TYPE', 'REFERENCES']
    missing = set(cols) - set(df.columns)
    error_msg = f'Missing columns: {missing}'
    assert len(missing) == 0, error_msg

    # Check NO empty values in mandatory cols
    cols_no_empty = [x for x in cols if x != 'STATION_NAME']
    empty = df[cols_no_empty].isnull().any()
    error_msg = f'Columns with empty values: {empty.index.tolist()}'
    assert empty.any() == False, error_msg

    # Check if coordinates are sufficiently close:
    # THERE ARE SEVERAL EVENTS WITH MACROSEISMIC VALUES VERY FAR FROM
    # THE EPICENTER. WE WHOULD TRY TO POLISH THE VALUES
    lon = df.LONGITUDE.max() - df.LONGITUDE.min()
    error_msg = f'Longitudes with +{lon} difference'
    assert abs(lon) < 35., error_msg
    lat = df.LATITUDE.max() - df.LATITUDE.min()
    error_msg = f'Latitudes with +{lat} difference'
    assert abs(lat) < 30., error_msg

    # Check empty columns
    empty = df.isnull().all()
    error_msg = f'All empty values in columns: {empty[empty].index.tolist()}'
    assert empty.any() == False, error_msg
    
    # Identify columns with IMT values
    imts = ['MMI', 'PGA', 'PGV', 
            'SA(0.3)', 'SA(0.6)', 'SA(1.0)', 'SA(2.0)', 'SA(3.0)']
    vals = [x[:-6] for x in df.columns if x.endswith('_VALUE')]
    sigma = [x[:-9] for x in df.columns if x.endswith('_LN_SIGMA')]
    if 'MMI_STDDEV' in df.columns:
        sigma.append('MMI')
    #  Each IMT has a corresponding uncertanty column
    missing = set(vals).difference(set(sigma))
    error_msg = f'IMTs missing uncertainty column: {missing}'
    assert set(vals) == set(sigma), error_msg
    # IMTs are supported in the suported list (imts)
    unknow = set(vals) - set(imts)
    error_msg = f'File contains unknow IMTs: {unknow}'
    assert set(imts).issuperset(set(vals)), error_msg
    
    # Check IMTs units
    if 'PGA_VALUE' in df.columns:
        max_val = df['PGA_VALUE'].max()
        error_msg = f'Check PGA values. PGA max = {max_val}'           
        
        # Exclude events with PGA > 2g
        exclude = [os.path.join('Middle_East', 'Iran', '19900620_M7.4_Manjil-Rudbar'),
                   os.path.join('Middle_East', 'Iran', '19970510_M7.2_Qayen'),
                   os.path.join('East_Asia', 'Japan', '20110311_M9.1_Tohoku'),
                   os.path.join('Europe', 'Italy', '20162017_Sequence_CentralItaly'),
                   os.path.join('Europe', 'Turkey', '19990817_M7.53_Izmit')]
        if not event in exclude:
            assert max_val <= 2, error_msg # To be increased if necessary
    
    if 'MMI_VALUE' in df.columns:
        max_val = df['MMI_VALUE'].max()
        error_msg = f'Check MMI units. MMI max = {max_val}'            
        assert max_val <= 10, error_msg

    # Ensure IMT values are above a certain threshold 
    # (Note: the OQ analysis fails if values are 0; negative values also should be avoided)
    for imt in imts:
        if f"{imt}_VALUE" in df.columns:
            min_val = df[f"{imt}_VALUE"].min()
            error_msg = f'Check {imt} values. {imt} min = {min_val} below min threshold'
            assert min_val > 1e-7, error_msg   

    # Check supported STATION_TYPE
    sup_types = ['seismic', 'macroseismic']
    in_types = df['STATION_TYPE'].unique()
    unknow = set(sup_types) - set(in_types)
    error_msg = f'unknow STATION_TYPE: {unknow}'
    assert set(sup_types).issuperset(set(in_types)), error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR README
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('event', df.Event_Path)
def test_readme_content(event):
    if event.find('_Sequence_') == -1:
        file_path = glob.glob(os.path.join(event, '3_Recording_Stations', 'README.md'))
        
        error_msg = "Required `README.md` file does not exist"
        assert len(file_path) > 0, error_msg
        
        # Open the README with a specified encoding to handle non-ASCII characters
        try:
            with open(file_path[0], 'r', encoding='utf-8') as readme:
                content = readme.read()
        except UnicodeDecodeError:
            # Fallback to another encoding if utf-8 fails
            with open(file_path[0], 'r', encoding='latin-1') as readme:
                content = readme.read()
        
        txt = '[](recording_stations.png)' 
        error_msg = "`recording_stations.png` not included in README"
        assert content.find(txt) != -1, error_msg

        txt = '## Reference datasets' 
        error_msg = "References not included in README"
        assert content.find(txt) != -1, error_msg

