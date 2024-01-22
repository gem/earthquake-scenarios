
<div align='center'>
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Global_Earthquake_Model_Logo.png/440px-Global_Earthquake_Model_Logo.png" alt="GEM Foundation" width="300"/>
</p>
<a href='./earthquake_scenarios/'>
    <img src='https://img.shields.io/badge/Earthquake_Scenarios-green?style=for-the-badge'>
</a>
<a href='./World/'>
    <img src='https://img.shields.io/badge/Global_coverage-gray?style=for-the-badge'>
</a>
<a href='./contribute_guidelines.md'>
    <img src='https://img.shields.io/badge/Contribute-orange?style=for-the-badge'>
</a>
<a href='LICENSE.txt'>
    <img src='https://img.shields.io/badge/LICENSE-blue?style=for-the-badge'>
</a>
</div>

# 🔎 GEM Earthquake Scenario Database

The development of probabilistic seismic risk assessment (PSRA) models requires stress-testing the various components of the models, often through the assessment of damage and losses considering the characteristics of past events[^1]. In this context, the GEM Foundation and its partners have expanded the OpenQuake scenario damage and loss calculator to use directly USGS ShakeMaps[^2][^3][^4], or earthquake data from other providers (e.g., INGV, EFEHR) or the scientific literature. This functionality allows users to generate cross-correlated ground motion fields considering recordings from seismic stations [^5], and to compute a number of risk metrics based on different rupture solutions and ground motion models, and to compare the results against past observations and damage reports. An overview of the functionalities implemented within the OpenQuake-engine can be found in https://github.com/gem/oq-engine/issues/8317.

# ✨ Overview

The Earthquake Scenario Database (ESD) aims at providing both earthquake and impact data for users to perform earthquake scenarios using GEM or their own models for validation and verification purposes. This database serves as a complement to the [USGS ShakeMap](https://earthquake.usgs.gov/data/shakemap/) Atlas and AtlasCat. The former resource has ShakeMaps for a comprehensive catalogue of nearly all near-damaging and damaging events worldwide for the past 120 years, and can be used directly for impact assessment within the OpenQuake-engine [^4]. The latter provides aggregate losses for each event separated by cause. The ESD builds upon these sources of data by collecting additional earthquake and impact information, often documented spatially and with greater detail.

> The v2023.0.0 release for the GEM's Earthquake Scenario Database is available! 🥳 🚀

<div align='left'>
    <img src="./World/eq_events.png" alt="GEM's ECD events" width="700"/>
</div>

This database is open and aims at being a community effort, that enables users to add new events (see [contributing guidelines](./contribute_guidelines.md)) or to provide additional data to existing entries. We aim to continue expanding the ESD by leveraging on data often collected within the scope of GEM projects, as well as data previously collected as part of the [GEM Earthquake Consequences Database](https://www.globalquakemodel.org/gempublications/Introduction-to-the-GEM-Earthquake-Consequences-Database-(GEMECD)).

## 🗺️ Database coverage

The following events are available in the database, and the global summary of impact data is available in the [World folder](./World).

<details>
<summary> Table with available events
</summary>

|     | Country                                 |   Year | Event_Name                                                                    |   Mw |   Depth_(km) | Max_Intensity_(MMI)          |
|----:|:----------------------------------------|-------:|:------------------------------------------------------------------------------|-----:|-------------:|:-----------------------------|
|   0 | Albania                                 |   2019 | [Durres](./Albania/20191126_M6.4_Albania)                                     | 6.4  |        22    | VIII                         |
|   1 | Algeria                                 |   2003 | [Boumerdes_2003](./Algeria/20030521_M6.8_Boumerdes)                           | 6.8  |        12    | IX-X                         |
|   2 | Australia                               |   1989 | [Newcastle](./Australia/19891227_M5.4_Newcastle)                              | 5.4  |        10    | VIII                         |
|   3 | Botswana                                |   2017 | [Moijabana_2017](./Botswana/20170403_M6.5_Moijabana)                          | 6.46 |        23.5  | VIII                         |
|   4 | Chile                                   |   1960 | [Valdivia_1960](./Chile/19600522_M9.5_Valdivia)                               | 9.5  |        25    | IX                           |
|   5 | Chile                                   |   2010 | [Maule_2010](./Chile/20100227_M8.8_Maule)                                     | 8.8  |        30    | VIII                         |
|   6 | Chile                                   |   2014 | [Iquique_2014](./Chile/20140401_M8.2_Iquique)                                 | 8.2  |        38.9  | VIII                         |
|   7 | Chile                                   |   2015 | [Illapel_2015](./Chile/20150916_M8.3_Illapel)                                 | 8.3  |        22.44 | VIII                         |
|   8 | Colombia                                |   1983 | [Popayán_1983 ](./Colombia/19830331_M5.6_Popayan)                             | 5.6  |        15    | VIII                         |
|   9 | Colombia                                |   1994 | [Cacua_1994](./Colombia/19940606_M6.8_Cauca)                                  | 6.8  |        10    | IX                           |
|  10 | Colombia                                |   1999 | [Armenia_1999](./Colombia/19990125_M6.1_Armenia)                              | 6.1  |        15    | IX                           |
|  11 | Colombia                                |   2004 | [Pizarro_2004](./Colombia/20041115_M7.2_Pizarro)                              | 7.2  |        15    | VIII                         |
|  12 | Colombia                                |   2008 | [Quetame_2008](./Colombia/20080524_M5.9_Quetame)                              | 5.9  |        10    | VII                          |
|  13 | Colombia                                |   2023 | [El Calvario](./Colombia/20230817_M6.1_ElCalvario)                            | 6.1  |        10    | VII                          |
|  14 | Costa Rica                              |   1991 | [Limon](./Costa_Rica/19910422_M7.6_Limon)                                     | 7.6  |        10    | VIII                         |
|  15 | Costa Rica                              |   2009 | [Cinchona](./Costa_Rica/20090108_M6.1_Cinchona)                               | 6.2  |         4.6  | IX in Cinchona e Isla Bonita |
|  16 | Costa Rica                              |   2012 | [Nicoya](./Costa_Rica/20120905_M7.6_Nicoya)                                   | 7.6  |        15.4  | VII                          |
|  17 | Costa Rica                              |   2017 | [Puntarenas_2017](./Costa_Rica/20171113_M6.5_Puntarenas)                      | 6.5  |        22    | VIII                         |
|  18 | Croatia                                 |   2020 | [Petrijna_2020](./Croatia/20201229_M6.3_Petrijna)                             | 6.4  |        10    | IX                           |
|  19 | Croatia                                 |   2020 | [Zagreb_2020](./Croatia/20200322_M5.1_Zagreb)                                 | 5.3  |        10    | VIII                         |
|  20 | Cyprus                                  |   1996 | [Cyprus](./Cyprus/19961009_M6.8_Cyprus)                                       | 6.8  |        33    | VI                           |
|  21 | Ecuador                                 |   2016 | [Pedernales_2016](./Ecuador/20160416_M7.8_Pedernales)                         | 7.8  |        17    | IX                           |
|  22 | Egypt                                   |   1992 | [Cairo_1992](./Egypt/19921012_M5.9_Cairo)                                     | 5.8  |        21.5  | VIII                         |
|  23 | El Salvador                             |   2001 | [Subduction_2001](./El_Salvador/20010113_M7.7_Subduction)                     | 7.7  |        39    | VIII                         |
|  24 | El Salvador                             |   2001 | [San Vicente](./El_Salvador/20010213_M6.6_SanVicente)                         | 6.6  |        13    | VIII                         |
|  25 | Greece                                  |   1981 | [GulfofCorinth_1981](./Greece/19810224_M6.7_GulfofCorinth)                    | 6.7  |        33    | IX                           |
|  26 | Greece                                  |   1981 | [GulfofCorinth_1981](./Greece/19810225_M6.4_GulfofCorinth)                    | 6.4  |        33    | IX                           |
|  27 | Greece                                  |   1981 | [GulfofCorinth_1981](./Greece/19810000_Sequence_GulfOfCorinth)                | 6.7  |        33    | IX                           |
|  28 | Greece                                  |   1986 | [Kalamata_1986](./Greece/19860913_M6.0_Kalamata)                              | 6    |        11.2  | X                            |
|  29 | Greece                                  |   1988 | [Elia_1988](./Greece/19881016_M5.88_Elia)                                     | 5.9  |        25.2  | VII                          |
|  30 | Greece                                  |   1995 | [Aigio_1995](./Greece/19950615_M6.4_Aigio)                                    | 6.5  |        14.2  | VIII                         |
|  31 | Greece                                  |   1995 | [KozaniGrevena_1995](./Greece/19950513_M6.5_KozaniGrevena)                    | 6.6  |        14    | VIII                         |
|  32 | Greece                                  |   1999 | [Athens_1999](./Greece/19990907_M5.9_Athens)                                  | 6    |        10    | IX                           |
|  33 | Greece                                  |   2014 | [Kefalonia_2014](./Greece/20140126_M6.1_Kefalonia)                            | 6.1  |         8    | VIII                         |
|  34 | Greece                                  |   2014 | [Kefalonia_2014](./Greece/20140203_M6.0_Kefalonia)                            | 6    |         5    | VII                          |
|  35 | Greece                                  |   2014 | [Kefalonia_2014](./Greece/20140000_Sequence_Kefalonia)                        | 6.1  |         8    | VII                          |
|  36 | Greece                                  |   2015 | [Lefkada_2015](./Greece/20151117_M6.5_Lefkada)                                | 6.5  |        11    | VIII                         |
|  37 | Greece                                  |   2017 | [AegeanSea_2017](./Greece/20170612_M6.3_AegeanSea)                            | 6.3  |        12    | VII                          |
|  38 | Greece                                  |   2020 | [AegeanSea_2020](./Greece/20201030_M7_AegeanSea)                              | 7    |        21    | VIII                         |
|  39 | Haiti                                   |   2010 | [Haiti](./Haiti/20100112_M7.0_Haiti)                                          | 7    |        13    | IX                           |
|  40 | Haiti                                   |   2021 | [Haiti](./Haiti/20210814_M7.2_Haiti)                                          | 7.2  |        10    | VIII                         |
|  41 | Iceland                                 |   2000 | [Iceland](./Iceland/20000617_M5.87_Iceland)                                   | 6.5  |        10    | VIII                         |
|  42 | Iceland                                 |   2000 | [Iceland_2000](./Iceland/20000620_M6.46_Iceland)                              | 6.5  |        10    | IX                           |
|  43 | Iceland                                 |   2008 | [Iceland_2008](./Iceland/20080529_M6.32_Iceland)                              | 6.3  |         9    | VIII                         |
|  44 | India, China, Nepal, Bhutan, Bangladesh |   2011 | [Sikkim_2011](./India, China, Nepal, Bhutan, Bangladesh/20110918_M6.9_Sikkim) | 6.9  |        50    | VIII                         |
|  45 | Indonesia                               |   2006 | [Yogyakarta](./Indonesia/20060527_M6.4_Yogyakarta)                            | 6.4  |        12.5  | VIII                         |
|  46 | Indonesia                               |   2009 | [Padang ](./Indonesia/20090930_M7.6_Padang)                                   | 7.6  |        81    | VIII                         |
|  47 | Iran                                    |   1978 | [Tabas](./Iran/19780916_M7.3_Tabas)                                           | 7.3  |        33    | IX                           |
|  48 | Iran                                    |   1990 | [Manjil-Rudbar](./Iran/19900620_M7.4_Manjil-Rudbar)                           | 7.4  |        18.5  | IX                           |
|  49 | Iran                                    |   1997 | [Qayen](./Iran/19970510_M7.2_Qayen)                                           | 7.2  |        10    | IX                           |
|  50 | Iran                                    |   1997 | [Golestan](./Iran/19970228_M6.1_Golestan)                                     | 6.1  |        10    | VIII                         |
|  51 | Iran                                    |   2003 | [Bam](./Iran/20031226_M6.6_Bam)                                               | 6.6  |        10    | IX                           |
|  52 | Iran                                    |   2005 | [Zarand](./Iran/20050222_M6.5_Zarand)                                         | 6.5  |        14    | VIII                         |
|  53 | Iran                                    |   2012 | [Ahar-Varzaghan](./Iran/20120811_M6.4_Ahar-Varzaghan)                         | 6.4  |        11    | VII                          |
|  54 | Iran                                    |   2012 | [Ahar-Varzaghan](./Iran/20120811_M6.2_Ahar-Varzaghan)                         | 6.2  |        12    | VIII                         |
|  55 | Iran                                    |   2012 | [Ahar-Varzaghan](./Iran/20120000_Sequence_Ahar-Varzaghan)                     | 6.4  |        11    | VII                          |
|  56 | Iran                                    |   2017 | [Sarpole-Zahab](./Iran/20171112_M7.3_SarpoleZahab)                            | 7.3  |        18.1  | IX                           |
|  57 | Italy                                   |   1980 | [Irpinia_1980](./Italy/19801123_M6.9_Irpinia)                                 | 6.9  |        10    | X                            |
|  58 | Italy                                   |   1990 | [Augusta_1990](./Italy/19901213_M5.61_Augusta)                                | 5.6  |        11.1  | VIII                         |
|  59 | Italy                                   |   1997 | [UmbriaMarche_1997](./Italy/19970000_Sequence_UmbriaMarche)                   | 5.7  |        10    | X                            |
|  60 | Italy                                   |   1997 | [UmbriaMarche_1997](./Italy/19971014_M5.86_UmbriaMarche)                      | 5.5  |        10    | VII                          |
|  61 | Italy                                   |   1997 | [UmbriaMarche_1997](./Italy/19970926_M5.97_UmbriaMarche)                      | 6    |        10    | VIII                         |
|  62 | Italy                                   |   1997 | [UmbriaMarche_1997](./Italy/19970926_M5.72_UmbriaMarche)                      | 5.7  |        10    | VIII                         |
|  63 | Italy                                   |   2002 | [Molise_2002](./Italy/20021031_M5.74_Molise)                                  | 5.9  |        10    | VII                          |
|  64 | Italy                                   |   2002 | [Molise_2002](./Italy/20021101_M5.72_Molise)                                  | 5.8  |        10    | VII                          |
|  65 | Italy                                   |   2002 | [Molise_2002](./Italy/20020000_Sequence_Molise)                               | 5.9  |        10    | VIII                         |
|  66 | Italy                                   |   2004 | [Gardone_2004](./Italy/20041124_M4.99_Gardone)                                | 5.1  |        17.2  | VIII                         |
|  67 | Italy                                   |   2009 | [Laquila_2009](./Italy/20090406_M6.18_Laquila)                                | 6.3  |         8.8  | VIII                         |
|  68 | Italy                                   |   2009 | [Laquila_2009](./Italy/20090407_M5.4_Laquila)                                 | 5.5  |        15.1  | VI                           |
|  69 | Italy                                   |   2009 | [Laquila_2009](./Italy/20090000_Sequence_Laquila)                             | 6.3  |         8.8  | X                            |
|  70 | Italy                                   |   2012 | [EmiliaRomagna_2012](./Italy/20120520_M5.8_EmiliaRomagna)                     | 6    |         6.3  | VIII                         |
|  71 | Italy                                   |   2012 | [EmiliaRomagna_2012](./Italy/20120529_M5.6_EmiliaRomagna)                     | 5.8  |        10.2  | VIII                         |
|  72 | Italy                                   |   2012 | [EmiliaRomagna_2012](./Italy/20120000_Sequence_EmiliaRomagna)                 | 6    |         6.3  | VIII                         |
|  73 | Italy                                   |   2016 | [CentralItaly_2016](./Italy/20161026_M6.09_CentralItaly)                      | 6.1  |        10    | VIII                         |
|  74 | Italy                                   |   2016 | [CentralItaly_2016](./Italy/20160824_M6.21_CentralItaly)                      | 6.2  |         4.44 | IX                           |
|  75 | Italy                                   |   2016 | [CentralItaly](./Italy/20162017_Sequence_CentralItaly)                        | 6.6  |         4.44 | IX                           |
|  76 | Italy                                   |   2016 | [CentralItaly_2016](./Italy/20161030_M6.5_CentralItaly)                       | 6.6  |         8    | IX                           |
|  77 | Italy                                   |   2017 | [CentralItaly_2017](./Italy/20170118_M5.95_CentralItaly)                      | 5.7  |         7    | VII                          |
|  78 | Japan                                   |   1995 | [Kobe_1995](./Japan/19950117_M6.9_Kobe)                                       | 6.9  |        21.9  | IX                           |
|  79 | Japan                                   |   2011 | [Tōhoku_2011](./Japan/20110311_M9.1_Tohoku)                                   | 9.1  |        29    | VIII                         |
|  80 | Japan                                   |   2016 | [Kumamoto_2016](./Japan/20160416_M7.0_Kumamoto)                               | 7    |        10    | IX                           |
|  81 | Japan                                   |   2018 | [Osaka_2018](./Japan/20180618_M5.5_Osaka)                                     | 5.5  |        10.3  | VIII                         |
|  82 | Japan                                   |   2018 | [HokkaidoEasternIburi_2018](./Japan/20180906_M6.6_HokkaidoEasternIburi)       | 6.6  |        35    | X                            |
|  83 | Japan                                   |   2019 | [Yamagata_2019](./Japan/20190618_M6.4_Yamagata)                               | 6.4  |        12    | VII                          |
|  84 | Mexico                                  |   1985 | [Mexico_Michoacan ](./Mexico/19850919_M8.1_Michoacan)                         | 8.1  |        15    | VII                          |
|  85 | Mexico                                  |   1999 | [Oaxaca_1999](./Mexico/19990930_M7.4_Oaxaca)                                  | 7.4  |        39    | VIII                         |
|  86 | Mexico                                  |   2017 | [Chiapas_2017](./Mexico/20170908_M8.2_Chiapas)                                | 8.2  |        45.9  | VII                          |
|  87 | Mexico                                  |   2017 | [Puebla_2017](./Mexico/20170919_M7.1_Puebla)                                  | 7.1  |        51.2  | VIII                         |
|  88 | Mexico                                  |   2021 | [Guerrero_2021](./Mexico/20210907_M7.1_Guerrero)                              | 7.1  |        10    | VIII                         |
|  89 | Mexico                                  |   2020 | [Oaxaca_2020](./Mexico /20200623_M7.4_Oaxaca)                                 | 7.4  |        22.6  | VIII                         |
|  90 | Morocco                                 |   2004 | [AlHoceima_2004](./Morocco/20040224_M6.3_AlHoceima)                           | 6.3  |        12.2  | IX                           |
|  91 | Nepal, India, China, Bangladesh         |   2015 | [Gorkha_2015](./Nepal, India, China, Bangladesh/20150425_M7.8_Gorkha)         | 7.8  |         8.22 | IX                           |
|  92 | Netherlands                             |   1992 | [Roermond_1992](./Netherlands/19920413_M5.3_Roermond)                         | 5.4  |        21.2  | VIII                         |
|  93 | New_Zealand                             |   2010 | [Canterbury_2010](./New_Zealand/20100904_M7.0_Canterbury)                     | 7    |        12    | VIII                         |
|  94 | New_Zealand                             |   2011 | [Christchurch_2011](./New_Zealand/20110222_M6.1_Christchurch)                 | 6.1  |         5.9  | IX                           |
|  95 | Pakistan, India, Afghanistan            |   2005 | [Kashmir](./Pakistan, India, Afghanistan/20051008_M7.6_Kashmir)               | 7.6  |        26    | IX                           |
|  96 | Peru                                    |   2007 | [Pisco_2007](./Peru/20070815_M7.9_Pisco)                                      | 7.9  |        40    | VIII                         |
|  97 | Romania                                 |   1990 | [Vrancea_1990](./Romania/19900531_M6.31_Vrancea)                              | 6.3  |        88.2  | V                            |
|  98 | Romania                                 |   1990 | [Vrancea_1990](./Romania/19900530_Sequence_Vrancea)                           | 7    |        89.3  | VIII                         |
|  99 | Romania                                 |   1990 | [Vrancea_1990](./Romania/19900530_M6.95_Vrancea)                              | 7    |        89.3  | VIII                         |
| 100 | Serbia                                  |   2010 | [Kraljevo](./Serbia/20101103_M5.52_Kraljevo)                                  | 5.5  |         0.9  | VI                           |
| 101 | Spain                                   |   2011 | [Lorca_2011](./Spain/20110511_M5.1_Lorca)                                     | 5.1  |         1    | VI                           |
| 102 | Tanzania, Uganda                        |   2016 | [Bukoba_2016](./Tanzania, Uganda/20160910_M5.9_Bukoba)                        | 5.9  |        40    | VII                          |
| 103 | Turkey                                  |   1992 | [Erzincan](./Turkey/19920313_M6.68_Erzincan)                                  | 6.7  |        27.2  | VIII                         |
| 104 | Turkey                                  |   1995 | [Dinar](./Turkey/19951001_M6.42_Dinar)                                        | 6.4  |        33    | VIII                         |
| 105 | Turkey                                  |   1998 | [AdanaCeyhan_1998](./Turkey/19980627_M6.28_AdanaCeyhan)                       | 6.3  |        33    | IV                           |
| 106 | Turkey                                  |   1999 | [Duzce_1999](./Turkey/19991112_M6.71_Duzce)                                   | 7.2  |        10    | IX                           |
| 107 | Turkey                                  |   1999 | [Izmit](./Turkey/19990817_M7.53_Izmit)                                        | 7.6  |        17    | X                            |
| 108 | Turkey                                  |   2011 | [Van_2011](./Turkey/20111023_M7.1_Van)                                        | 7.1  |        18    | VIII                         |
| 109 | Turkey                                  |   2023 | [CentralTurkey_2023](./Turkey/20230206_M7.8_KahramanmarasGaziantep)           | 7.8  |        10    | XII                          |

</details>

# 🚀 Model versions

Each version of the archive that is released can be accessed by changing from the `main` branch to the `tag` of a given version.
The `main` branch could contain the work-in-progress of the next version of the model.

| Version   | Release Notes                                                            |
|-----------|--------------------------------------------------------------------------|
| [v2023.0.0](https://github.com/gem/ecd/tree/v2023.0.0) | First release with 100 earthquake scenario events.|

# 📚 Publications

Please cite the work as follows:

GEM Foundation (2023), GEM Earthquake Scenario Database, GitHub. 
[https://github.com/gem/earthquake-scenarios](https://github.com/gem/earthquake-scenarios)/

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8425465.svg)](https://doi.org/10.5281/zenodo.8425465)


# 🌟 Contributors

The authors are grateful for the input from dozens of collaborators. 

# License
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

# 🤔 Frequently asked questions

### How to contribute?

You can follow the instructions indicated in the [contributing guidelines](./contribute_guidelines.md).

### Which version am I seeing? How to change the version?

By default, you will see the files in the repository in the `main` branch. Each version of the model that is released can be accessed is marked with a `tag`. By changing the tag version at the top of the repository, you can change see the files for a given version.

Note that the `main` branch could contain the work-in-progress of the next version of the model.

### How do I download the data for a given version?

For each version, a related zip file is available in the [release section](https://github.com/gem/global_exposure_model/releases).

# References
[^1]: Villar-Vega, M., Silva, V. (2017). Assessment of earthquake damage considering the characteristics of past events in South America. Earthquake Engineering and Soil Dynamics, 99:86-96.
[^2]: Silva V, Horspool N (2019). Combining USGS ShakeMaps and the OpenQuake-engine for damage and loss assessment. Earthquake Engineering and Structural Dynamics. 48(6):634-652.
[^3]: Worden, C. B., Thompson, E. M., Hearne, M. G., & Wald, D. J. (2020). ShakeMap Manual Online: technical manual, user’s guide, and software guide, U. S. Geological Survey. URL: http://usgs.github.io/shakemap/. DOI: https://doi.org/10.5066/F7D21VPQ.
[^4]: Wald, D. J., Worden, C. B., Thompson, E. M., & Hearne, M. G. (2022). ShakeMap operations, policies, and procedures. Earthquake Spectra, 38(1), 756–777. DOI: https://doi.org/10.1177/87552930211030298.
[^5]: Engler, D. T., Worden, C. B., Thompson, E. M., & Jaiswal, K. S. (2022). Partitioning Ground Motion Uncertainty When Conditioned on Station Data. Bulletin of the Seismological Society of America, 112(2), 1060–1079. DOI: https://doi.org/10.1785/0120210177.
