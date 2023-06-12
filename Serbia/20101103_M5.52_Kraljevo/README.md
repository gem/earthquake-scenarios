# 🌎 2010 M5.5 Kraljevo earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2010 M5.5 Kraljevo earthquake in Serbia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2010 Serbia earthquake (also referred to as the Kraljevo earthquake) occurred on 3 November in central Serbia just several kilometers from Kraljevo. The earthquake had a magnitude of 5.5 and a maximum Mercalli intensity of VI (Strong). The shock was felt across the country, including the capital Belgrade, and in neighboring countries. Two people were killed and over 100 suffered light injuries. There were 5,967 structures that sustained some damage, 1,551 declared unsafe for use and require repairment, and 138 were damaged beyond repair. There were more than 350 aftershocks, including a magnitude Mwr 4.3 earthquake on November 4.
[Wikipedia](https://en.wikipedia.org/wiki/2010_Serbia_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2010                                                                   |
| Country              | Serbia                                                                 |
| Region               | Kraljevo                                                               |
| Event_Name           | Kraljevo                                                               |
| Local_Date           | 03/11/2010                                                             |
| Local_Time           | 00:56:55                                                               |
| Latitude             | 43.76                                                                  |
| Longitude            | 20.73                                                                  |
| Depth_(km)           | 0.9                                                                    |
| Mw                   | 5.5                                                                    |
| Max_Intensity_(MMI)  | VI                                                                     |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 2                                                                      |
| Injured              | 100-120                                                                |
| Displaced_Population | 1470                                                                   |
| Affected_Population  | 25440                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 5000-5967 Buildings                                                    |
| Collapsed_Units      | 1000-1550 Buildings                                                    |
| Economic_Losses      | 0-138 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000hny4/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2010_Serbia_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
