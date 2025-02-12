# -------------------------------------------------------------------------------------
#   CONFIGURATION
# -------------------------------------------------------------------------------------

# Dependencies
import os, glob
import pandas as pd
import pytest

# -------------------------------------------------------------------------------------
#   INITIALIZATION
# -------------------------------------------------------------------------------------

# Determine all relevant country folders
skip_folders = ['src', 'tests', 'World']

regions = sorted([folder for folder in next(os.walk('.'))[1] if folder
                not in skip_folders
                and not folder.startswith(".")])
    
events = glob.glob('**/*_M*/', recursive=True)

# Arrange DataFrame with event paths
df = pd.DataFrame({'Event_Path':events}).explode('Event_Path')
df['Region'] = df.Event_Path.str.split(os.sep, expand=True)[0]
df['Country'] = df.Event_Path.str.split(os.sep, expand=True)[1]
df['Event_Folder'] = df.Event_Path.str.split(os.sep, expand=True)[2]

# Include events within a sequence
sequence = df.Event_Path.str.split(os.sep, expand=True)[3]
df.loc[sequence != '', 'Event_Folder'] = sequence[sequence != '']

# Ignore folders marked as DRAFT
ignore = True
if ignore:
    draft_prefix = "DRAFT_"
    edx = df.Event_Folder.str.startswith(draft_prefix) # non-draft indices
    df = df[~edx]


# -------------------------------------------------------------------------------------
#   CHECK FOR EMPTY FOLDERS
# -------------------------------------------------------------------------------------

# Check or empty folders
@pytest.mark.parametrize('country', df.Country.unique())
def test_empty_country_folder(country):
    idx = df.Country == country
    check_null = df.loc[idx, 'Event_Folder'].isnull().values.all()
    error_msg = f"No event folders found for {country}"
    assert not check_null, error_msg


# -------------------------------------------------------------------------------------
#   CHECK FOR EVENT NAME FORMAT
# -------------------------------------------------------------------------------------

# Check that event name folder follows required format
@pytest.mark.parametrize('event', df.Event_Folder)
def test_event_name(event):
    # Count number of components
    str_split = event.split("_")
    fmt_msg = f"{event} does not satisfy event name format: <DATE>_<MAG>_<NAME>"
    assert len(str_split) == 3, fmt_msg
    # Check date format
    date = str_split[0]
    dtm_msg = f"{date} substring of {event} does not satisfy date format: YYYYMMDD"
    assert len(date) == 8, dtm_msg
    # Check magnitude format
    mag = str_split[1]
    if not mag == "Sequence":
        mag_msg = f"{mag} substring of {event} does not satisfy magnitude format: MX.X"
        # assert re.match(r"M[0-9].[0-9]", mag), mag_msg
        assert mag.startswith("M"), mag_msg
    
    
# -------------------------------------------------------------------------------------
#   CHECK FOR MINIMUM REQUIRED FOLDERS AND FILES
# -------------------------------------------------------------------------------------
    
# Check for README file
@pytest.mark.parametrize('event', df.Event_Path)
def test_readme_file_exists(event):
    file_path = os.path.join(event, "README.md")
    error_msg = f"Required readme ({file_path}) does not exist"
    assert os.path.exists(file_path), error_msg
    
# Check for required folders
required_subfolders = [
    os.path.join("1.Impact"),
    os.path.join("2.Rupture"),
    os.path.join("3.Recording_Stations"),
    os.path.join("4.OpenQuake_gmfs"),
]
@pytest.mark.parametrize('subfolder', required_subfolders)
@pytest.mark.parametrize('event', df.Event_Path)
def test_event_subfolders_exist(event, subfolder):
    if event.find('_Sequence_') == -1:
        folder_path = os.path.join(event, subfolder)
        error_msg = f"Required subfolder {folder_path} does not exist"
        assert os.path.exists(folder_path), error_msg


# # Check for OQ GMFs CSV
# @pytest.mark.parametrize('event', df.Event_Path)
# def test_oq_gmfs_exist(event):
#     oq_path = os.path.join(event, "OpenQuake_gmfs")
#     file_path = os.path.join(oq_path, "gmf_scenario.csv")
#     error_msg = f"Required OQ input ({file_path}) does not exist"
#     if os.path.exists(oq_path):
#         assert os.path.exists(file_path), error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass

# # Check for OQ GMFs CSV
# @pytest.mark.parametrize('event', df.Event_Path)
# def test_oq_job_exists(event):
#     oq_path = os.path.join(event, "OpenQuake_gmfs")
#     prefix, suffix = "job", ".ini"
#     if os.path.exists(oq_path):
#         job_files = [file for file in os.listdir(oq_path)
#                      if file.startswith(prefix) and file.endswith(suffix)]
#         error_msg = f"At least one OQ job does not exist in {oq_path}"
#         assert len(job_files) > 0, error_msg
#     else: # avoid duplicate check on required (sub)folders
#         pass
