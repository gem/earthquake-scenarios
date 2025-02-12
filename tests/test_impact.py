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
db = pd.DataFrame({'Event_Path':events}).explode('Event_Path')
db.Event_Path = db.Event_Path.apply(lambda x: os.path.normpath(x))
db['Region'] = db.Event_Path.str.split(os.sep, expand=True)[0]
db['Country'] = db.Event_Path.str.split(os.sep, expand=True)[1]
db['Event_Folder'] = db.Event_Path.str.split(os.sep, expand=True)[2]

# Include events within a sequence
sequence = db.Event_Path.str.split(os.sep, expand=True)[3]
db.loc[sequence != '', 'Event_Folder'] = sequence[sequence != '']
db.loc[sequence != '','Sequence'] = True

# Find all individual files with recording stations
files = glob.glob(os.path.join('**', '1.Impact', 'Impact_*.csv'),
                     recursive=True)

# Ignore folders marked as DRAFT
ignore = True
if  ignore:
    draft_prefix = "DRAFT_"
    edx = db.Event_Folder.str.startswith(draft_prefix) # non-draft indices
    if edx.any():
        db = db[~edx]
    files = [x for x in files if x.find('DRAFT_') == -1]


# -----------------------------------------------------------------------------
#   CHECKS THAT Impact_All_ID_0 FILE EXISTS
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', db.Event_Path)
def test_impact_exist(event):
    eq_info = glob.glob(os.path.join(event, '1.Impact', 'Impact_All_ID_0.csv'))
    sequence = db.loc[db.Event_Path == event, 'Sequence'].item()

    error_msg = "The file `Impact_All_ID_0.csv` is required"
    if not sequence: 
        assert len(eq_info) == 1, error_msg
    

# -----------------------------------------------------------------------------
#   CHECK FILE CONTENT
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('file_path', files)
def test_impact_contents(file_path):

    df = pd.read_csv(file_path)

    # Get file information
    file_name = os.path.basename(file_path)
    idx = file_path[-5:-4]

    # Mandatory columns:
    if idx in ['0', '1']:
        mandatory = [f'ID_{idx}', f'NAME_{idx}', 'REFERENCE', 'COMMENTS']
    else:
         mandatory = [f'NAME_{idx}', 'REFERENCE', 'COMMENTS']       
    building = ['AFFECTED_UNITS', 'DAMAGED_UNITS', 'COLLAPSED_UNITS',
                'UNIT_TYPES']
    humans = ['FATALITIES', 'FATALITIES_GROUND_SHAKING', 'INJURIES',
              'DISPLACED_POPULATION', 'AFFECTED_POPULATION']
    impact = ['ECONOMIC_LOSSES', 'INSURED_LOSSES', 'CURRENCY', 
              'INDUCED_EFFECTS', 'FLAG']

    # Check mandatory columns in impact files:
    if file_name.find('Impact_All_ID_') == 0:
        cols = mandatory + building + humans + impact
    elif file_name.find('Impact_Buildings_ID_') == 0:
        cols = mandatory + building
    elif file_name.find('Impact_Human_ID_') == 0:
        cols = mandatory + humans
    else:
        pytest.skip(f"File {file_name} not recognised as Impact information")
    
    if file_path.find(os.path.join('src', 'Event_Template')) != -1:
        pytest.skip("Skip `Event_Template` information")
        
    # Create DataFrame with impact data
    df = pd.read_csv(file_path, encoding='utf-8')
    
    # Check empty files:
    error_msg = f"Empty file: {file_name}"
    assert df.empty == False, error_msg         
        

    missing = set(cols).difference(set(df.columns))
    error_msg = f"Columns {sorted(missing)} missing in {file_name}"
    assert len(missing) == 0, error_msg
    
    # # Check no empty values in columns:
    # no_empty = [f'ID_{idx}', f'NAME_{idx}', 'REFERENCE']
    # empty = df[no_empty].isna()
    # error_msg = f"Empty values in columns {no_empty}"
    # assert empty.any().any() == False, error_msg
