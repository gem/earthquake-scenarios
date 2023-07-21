# -----------------------------------------------------------------------------
#   CONFIGURATION
# -----------------------------------------------------------------------------

# Dependencies
import os
import glob
import pandas as pd
import pytest

# -------------------------------------------------------------------------------------
#   INITIALIZATION
# -------------------------------------------------------------------------------------

# Determine all relevant country folders
skip_folders = ["src", "tests"]
countries = [folder for folder in next(os.walk('.'))[1] if folder
                not in skip_folders
                and not folder.startswith(".")]
    
# Determine all relevant event folders, including sequences
events = []
for country in countries:
    for folder in next(os.walk(country))[1]:
        events.append(os.path.join(country, folder))
        if '_Sequence_' in folder:
            subfolders = next(os.walk(os.path.join(country, folder)))[1]
            if 'Impact' in subfolders:
                subfolders.remove('Impact')
            if 'References' in subfolders:
                subfolders.remove('References')
            events.append([os.path.join(country, folder, sequence)
                        for sequence in subfolders])

# Arrange DataFrame with event paths
db = pd.DataFrame({'Event_Path':events}).explode('Event_Path')
db['Country'] = db.Event_Path.str.split(os.sep, expand=True)[0]
db['Event_Folder'] = db.Event_Path.str.split(os.sep, expand=True)[1]

# Include events within a sequence
sequence = db.Event_Path.str.split(os.sep, expand=True)[2]
db.loc[~sequence.isna(), 'Event_Folder'] = sequence[~sequence.isna()]
db.loc[~sequence.isna(),'Sequence'] = True

# Ignore folders marked as DRAFT
ignore = True
if ignore:
    draft_prefix = "DRAFT_"
    edx = db.Event_Folder.str.startswith(draft_prefix) # non-draft indices
    db = db[~edx]


# -----------------------------------------------------------------------------
#   CHECKS THAT A SUMMARY FILE EXISTS
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', db.Event_Path)
def test_eq_info_exist(event):
    eq_info = glob.glob(os.path.join(event, 'earthquake_information.csv'))
        
    error_msg = "The file `earthquake_information.csv` is required"
    assert len(eq_info) == 1, error_msg
    

# -----------------------------------------------------------------------------
#   CHECK FILE CONTENT
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', db.Event_Path)
def test_format(event):
    file_path = glob.glob(os.path.join(event, 'earthquake_information.csv'))[0]

    sequence = db.loc[db.Event_Path == event, 'Sequence'].item()

    # Create DataFrame with eq information
    df = pd.read_csv(file_path, index_col='FIELD', encoding='utf-8')

    # Check the file has only one column:
    assert len(df.columns) == 1, 'earthquake_information.csv must have only 2 columns `FIELD` and `DESCRIPTION`'

    # Check no empty values in columns:
    no_empty = ['Year', 'Country', 'Region', 'Event_Name', 'Local_Date',
            'Local_Time', 'Latitude', 'Longitude', 'Depth_(km)', 'Mw',
            'Max_Intensity_(MMI)', 'Fault_mechanism', 'Tectonic_region_type',
            'USGS page', 'Wikipedia page']
    empty = df.loc[no_empty, 'DESCRIPTION'].isna()
    error_msg = "The earthquake summary mandatory columns have empty values"
    assert empty.any() == False, error_msg
        
    # Check year format
    year = int(df.loc['Year', 'DESCRIPTION'])
    error_msg = f"{year} substring does not satisfy date format: YYYY"
    assert year > 1900 and year < 2024, error_msg

    # Check date format
    date = df.loc['Local_Date', 'DESCRIPTION']
    day, month, year = date.split('/')
    error_msg = f"{date} substring does not satisfy date format: DD/MM/YYYY"
    assert (len(date) == 10 and int(day) <= 31 and int(month) <= 12 and 
            int(year) > 1900 and int(year) < 2024), error_msg

    # Check time format
    time = df.loc['Local_Time', 'DESCRIPTION']
    hh, mm, ss = time.split(':')
    error_msg = f"{time} substring does not satisfy date format: HH:MM:SS"
    assert (len(time) == 8 and len(hh) == 2 
            and len(mm) == 2 and len(ss) == 2), error_msg
    assert (int(hh) <= 59 and int(mm) <= 59 and int(ss) <= 59), error_msg

    # Check coordinates
    coords = df.loc[[ 'Longitude', 'Latitude'], 'DESCRIPTION']
    lon = abs(float(coords.Longitude)) < 180
    lat = abs(float(coords.Latitude)) < 90
    error_msg = "Coordinates out of rages"
    assert (lon and lat), error_msg

    # CHECKS FOR IMPACT DATA
    # Ignore this check for events within a sequence (not the main event)
    if not sequence: 

       # Check no empty values in columns:
        csq = ['Fatalities', 'Injured', 'Displaced_Population', 
            'Affected_Population', 'Affected_Units', 'Damaged_Units', 
            'Collapsed_Units', 'Economic_Losses', 'Insured_Losses']
        empty = df.loc[csq, 'DESCRIPTION'].isna()
        error_msg = "At least one consequence value is required"
        assert empty.all() == False, f'sequence, {error_msg}'
    
        # # TO ADD TEST LATER WHEN MODELLERS REVIEW THE DATA    

        # # Check units for damaged structures:
        # units = df.DESCRIPTION.str.contains(' Units')
        # error_msg = "Specify the unit of impacted structures (Buildings, Dwelling or Households)"
        # assert units.any() == False, error_msg    

        # Check economic impact is reported in Million:
        eco = df.loc[['Economic_Losses', 'Insured_Losses']]
        eco.DESCRIPTION.fillna('', inplace=True)
        for value in eco.DESCRIPTION:
            if value != '':
                vals = str(value).split(' ')    
                error_msg = f"{value}: Economic impact should be in Million followed by currency string (e.g., 300 M USD)"
                assert len(vals) >= 3, error_msg 
                assert (vals[1] == 'M' and len(vals[2]) == 3), error_msg 
