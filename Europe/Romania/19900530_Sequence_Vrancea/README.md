# 🌎 1990 M7 Vrancea earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1990 M7 Vrancea earthquake in Romania.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1990 Vrancea earthquakes were three earthquakes on 30 and 31 May 1990 with magnitudes of 7.0 Mw and 6.2 Mw  that struck the Romanian county of Vrancea, on two consecutive days. Severe damage in the Bucharest-Brăila-Brașov area was reported and dozens of casualties in Romania and neighbouring Moldova, Ukraine and Bulgaria.
The seismic doublet of May 1990 consisted of two mainshocks occurred at a distance of only 13 hours. The first mainshock took place in the afternoon of 30 May 1990, at 13:40:06 (local hour). The epicenter was located in the northeastern part of the Vrancea Mountains (45.9°N 26.9°E﻿ / 45.9; 26.9), at a depth of 89 km. The earthquake had a magnitude of MGR  6.7 or Mw  6.9, the intensity in the epicentral area being of VIII degrees on the Mercalli intensity scale, and VII degrees in Bucharest. On the morning of 31 May 1990, at 3:17 (local hour), occurred the second mainshock, at a depth of 79–86 km, having the magnitude MGR  6.1 or Mw  6.3. The event was felt in the epicentral area with an intensity of VII degrees on the Mercalli intensity scale, and VI degrees in Bucharest; likewise, the quake was felt strong enough in Dobruja.
In the USGS EXPO-CAT database it is estimated that during this earthquake 355,000 people were exposed to intensity VII, of which around 61% were in rural areas.
[Wikipedia](https://en.wikipedia.org/wiki/1990_Vrancea_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1990                                                                   |
| Country              | Romania                                                                |
| Region               | Vrancea                                                                |
| Event_Name           | Vrancea_1990                                                           |
| Local_Date           | 30/05/1990                                                             |
| Local_Time           | 10:40:06                                                               |
| Latitude             | 45.841                                                                 |
| Longitude            | 26.668                                                                 |
| Depth_(km)           | 89.3                                                                   |
| Mw                   | 7                                                                      |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 9-14                                                                   |
| Injured              | 700                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 0-23.7 M USD                                                           |
| Insured_Losses       | 0-23.7 M USD                                                           |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp00049yk/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1990_Vrancea_earthquakes                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
