# -----------------------------------------------------------------------------
#   CONFIGURATION
# -----------------------------------------------------------------------------

# Dependencies
import os
import pandas as pd
import pytest
import glob

from openquake.hazardlib import sourceconverter, nrml
from src.get_rupture_info import repture_xml_to_df


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

# Ignore folders marked as DRAFT
ignore = True
if ignore:
    draft_prefix = "DRAFT_"
    edx = df.Event_Folder.str.startswith(draft_prefix) # non-draft indices
    if edx.any():
        df = df[~edx]


# -----------------------------------------------------------------------------
#   CHECKS THAT AT LEAST ONE RUPTURE FILE EXISTS
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df.Event_Path)
def test_rupture_files_exist(event):        
    ruptures = glob.glob(os.path.join(event, "2_Rupture", 
                                      'earthquake_rupture_model_*.xml'))
    error_msg = "At least one `earthquake_rupture_model_*.xml` required"
    if event.find('_Sequence_') == -1:
      assert len(ruptures) > 0, error_msg


# -----------------------------------------------------------------------------
#   CHECKS RUPTURE WITH OQ FORMAT
# -----------------------------------------------------------------------------

ruptures = glob.glob(os.path.join('**', 'earthquake_rupture_model_*.xml'),
                     recursive=True)

@pytest.mark.parametrize('rup_file', ruptures)
def test_oq_rupture_file(rup_file):
    get_rupture(rup_file)

def get_rupture(filename):
    [rup_node] = nrml.read(filename)
    conv = sourceconverter.RuptureConverter(rupture_mesh_spacing=2)
    rup = conv.convert_node(rup_node)
    return rup


# -----------------------------------------------------------------------------
#   CHECK INFORMATION ACROSS RUPTURE FILES
# -----------------------------------------------------------------------------
    
@pytest.mark.parametrize('event', df.Event_Path)
def test_rupture_info(event):
    ruptures = glob.glob(os.path.join(event, "2_Rupture", 
                                      'earthquake_rupture_model_*.xml'))
    
    if len(ruptures) > 0:
        # Create DataFrame with rupture information
        df = [ ]
        for rupfile in sorted(ruptures):
            source = os.path.basename(rupfile)
            # print(source)
            _, rup_df = repture_xml_to_df(rupfile)
            rup_df.index = [source]
            df.append(rup_df)    
        df = pd.concat(df)

        # Check that STRIKES are consistent
        dif = df.strike - df.strike.min()
        dmax = dif.max()
        if dmax != dmax:
            dmax = 0 # No value reported
        elif dmax > 180:
            # Find smaller angle (useful when strikes are close to 0 or 360)
            dmax = abs((dmax + 180) % 360 - 180)
        error_msg = f"Rupture strikes with {dmax} difference > 60 degrees"
        # Exclude specific events with strikes close to 90 or 270
        exclude = [os.path.join('Caribbean_Central_America', 'El_Salvador', '20010213_M6.6_SanVicente'),
                   os.path.join('Middle_East', 'Iran', '19970510_M7.2_Qayen'),
                   os.path.join('Middle_East', 'Iran', '20120000_Sequence_Ahar-Varzaghan', '20120811_M6.2_Ahar-Varzaghan'),
                   os.path.join('Middle_East', 'Iran', '20120000_Sequence_Ahar-Varzaghan', '20120811_M6.4_Ahar-Varzaghan'),
                   os.path.join('Europe', 'Greece', '19950513_M6.5_KozaniGrevena'),
                   os.path.join('Europe', 'Croatia', '20201229_M6.3_Petrijna'),
                   os.path.join('Europe', 'Greece', '20170612_M6.3_AegeanSea'),
                   os.path.join('Europe', 'Greece', '19860913_M6.0_Kalamata'),
                   os.path.join('Europe', 'Italy', '19970000_Sequence_UmbriaMarche', '19970926_M5.72_UmbriaMarche'),
                   os.path.join('Europe', 'Italy', '19970000_Sequence_UmbriaMarche', '19970926_M5.97_UmbriaMarche'),
                   os.path.join('Europe', 'Italy', '19970000_Sequence_UmbriaMarche', '19971014_M5.86_UmbriaMarche'),
                   os.path.join('Europe', 'Italy', '20020000_Sequence_Molise', '20021031_M5.74_Molise'),
                   os.path.join('Europe', 'Turkey', '19990817_M7.53_Izmit'),
                   os.path.join('Europe', 'Turkey', '20201030_M7_AegeanSea'),
                   os.path.join('Europe', 'Turkey', '20230206_M7.8_KahramanmarasGaziantep'),
                   os.path.join('Europe', 'Spain', '20110511_M5.1_Lorca')]
        if not event in exclude:
            assert dmax < 60, error_msg
        
        # Check that DIPS are consistent
        vmin = df.dip.min()
        vmax = df.dip.max()
        dif = vmax - vmin
        if dif != dif:
            dif = 0 # No value reported
        error_msg = f"Rupture dips with {dif} difference > 25 degrees"
        # Exclude specific events with large dip differences
        exclude = [os.path.join('North_America', 'Mexico', '20210907_M7.1_Guerrero'),
                   os.path.join('Europe', 'Albania', '20191126_M6.4_Albania'),
                   os.path.join('Europe', 'Netherlands', '19920413_M5.3_Roermond'),
                   os.path.join('South_America', 'Colombia', '20230817_M6.1_ElCalvario'),
                   os.path.join('Europe', 'Croatia', '20201229_M6.3_Petrijna'),
                   os.path.join('Europe', 'Greece', '19881016_M5.88_Elia'),
                   os.path.join('Europe', 'Greece', '19810000_Sequence_GulfOfCorinth', '19810225_M6.4_GulfofCorinth'),
                   os.path.join('Europe', 'Italy', '20162017_Sequence_CentralItaly', '20161030_M6.5_CentralItaly'),
                   os.path.join('Middle_East', 'Iran', '20120000_Sequence_Ahar-Varzaghan', '20120811_M6.4_Ahar-Varzaghan'),
                   os.path.join('Europe', 'Turkey', '19951001_M6.42_Dinar'),
                   os.path.join('Europe', 'Turkey', '20111023_M7.1_Van'),
                   os.path.join('Europe', 'Spain', '20110511_M5.1_Lorca'),
                   os.path.join('Middle_East', 'Iran', '19970228_M6.1_Golestan')]
        if not event in exclude:
            assert abs(dif) < 25, error_msg

        # Check that RAKEs are consistent
        vmin = df.rake.min()
        vmax = df.rake.max()
        dif = vmax - vmin
        if dif != dif:
            dif = 0 # No value reported
        error_msg = f"Rupture rakes with {dif} difference > 40 degrees"
        # Exclude specific events with large rake differences
        exclude = [os.path.join('South_America', 'Chile', '19600522_M9.5_Valdivia'),
                   os.path.join('South_America', 'Chile', '20150916_M8.3_Illapel'),
                   os.path.join('Caribbean_Central_America', 'Costa_Rica', '20171113_M6.5_Puntarenas'),
                   os.path.join('Southeast_Asia', 'Indonesia', '20060527_M6.4_Yogyakarta'),
                   os.path.join('Middle_East', 'Iran', '19780916_M7.3_Tabas'),
                   os.path.join('Middle_East', 'Iran', '19900620_M7.4_Manjil-Rudbar'),
                   os.path.join('Middle_East', 'Iran', '20120000_Sequence_Ahar-Varzaghan', '20120811_M6.2_Ahar-Varzaghan'),
                   os.path.join('Middle_East', 'Iran', '20120000_Sequence_Ahar-Varzaghan', '20120811_M6.4_Ahar-Varzaghan'),
                   os.path.join('Europe', 'Croatia', '20200322_M5.1_Zagreb'),
                   os.path.join('Europe', 'Croatia', '20201229_M6.3_Petrijna'),
                   os.path.join('Europe', 'Greece', '19881016_M5.88_Elia'),
                   os.path.join('Europe', 'Greece', '19810000_Sequence_GulfOfCorinth', '19810225_M6.4_GulfofCorinth'),
                   os.path.join('Europe', 'Italy', '19901213_M5.61_Augusta'),
                   os.path.join('Europe', 'Italy', '20020000_Sequence_Molise', '20021031_M5.74_Molise'),
                   os.path.join('Europe', 'Italy', '20041124_M4.99_Gardone'),
                   os.path.join('Europe', 'Italy', '20090000_Sequence_Laquila', '20090407_M5.4_Laquila'),
                   os.path.join('Europe', 'Turkey', '19920313_M6.68_Erzincan'),
                   os.path.join('Europe', 'Turkey', '20111023_M7.1_Van'),
                   os.path.join('Oceania', 'Australia', '19891227_M5.4_Newcastle')]
        if not event in exclude:
            assert abs(dif) < 40, error_msg

        # Check MAGNITUDE consistence
        mag = float(event.split('_')[-2].replace('M',''))
        vmin = df.mag.min()
        vmax = df.mag.max()
        dif = max(abs(vmax - mag), abs(vmin - mag))
        error_msg = f"Magnitudes differing > 0.5 units with respect to Mw {mag}"
        exclude = [os.path.join('Europe', 'Iceland', '20000617_M5.87_Iceland')]
        if not event in exclude:
            assert abs(dif) < 0.5, error_msg

        # Check that DEPTH are consistent
        vmin = df.depth.min()
        vmax = df.depth.max()
        dif = vmax - vmin
        error_msg = f"Rupture depths with {dif} difference > 25 km"
        # Exclude specific events with differing depth data
        exclude = [os.path.join('South_America', 'Colombia', '19830331_M5.6_Popayan'),
                   os.path.join('North_America', 'Mexico', '20170908_M8.2_Chiapas'),
                   os.path.join('Middle_East', 'Iran', '19780916_M7.3_Tabas'),
                   os.path.join('Europe', 'Greece', '19810000_Sequence_GulfOfCorinth', '19810224_M6.7_GulfofCorinth'),
                   os.path.join('Europe', 'Greece', '19810000_Sequence_GulfOfCorinth', '19810225_M6.4_GulfofCorinth'),
                   os.path.join('Europe', 'Turkey', '19951001_M6.42_Dinar')]
        if not event in exclude:
            assert abs(dif) < 25, error_msg


# -----------------------------------------------------------------------------
#   CHECKS FOR README
# -----------------------------------------------------------------------------

@pytest.mark.parametrize('event', df.Event_Path)
def test_readme_content(event):
    file_path = glob.glob(os.path.join(event, '2_Rupture', 'README.md'))
    
    if event.find('_Sequence_') == -1:
        # Check that README exists
        error_msg = "Missing README file"
        assert len(file_path) == 1, error_msg
        
        # Attempt to open the README file with UTF-8 encoding first
        try:
            with open(file_path[0], 'r', encoding='utf-8') as readme:
                content = readme.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, try reading with 'latin-1' encoding
            with open(file_path[0], 'r', encoding='latin-1') as readme:
                content = readme.read()
        except FileNotFoundError:
            # Handle file not found error
            raise Exception(f"README file {file_path[0]} not found.")
        except Exception as e:
            # Handle any other unforeseen errors
            raise Exception(f"An error occurred while reading {file_path[0]}: {str(e)}")

        # Check that image with ruptures exists
        txt = '[](earthquake_ruptures.png)'
        error_msg = "`earthquake_ruptures.png` not included in README"
        assert content.find(txt) != -1, error_msg
        
        # Check that References are included
        txt = '## References' 
        error_msg = "References not included in README"
        assert content.find(txt) != -1, error_msg
        
        # Check that table with rupture details exists
        txt = '## Rupture details\n' 
        error_msg = 'Missing `Rupture details` in README'
        assert content.find(txt) != -1, error_msg
        
        # Verify content for rupture details
        for txt in ['Fault mechanism', 'Tectonic region type']:
            line = [line for line in content.split('\n') if txt in line][0]
            line = line.replace(' ', '')
            value = line.split('|')[2]
            assert value != '', f'Missing `{txt}` in README'
