# 🌎 2020 M5.3 Zagreb earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2020 M5.3 Zagreb earthquake in Croatia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

At approximately 6:24 AM CET on the morning of 22 March 2020, an earthquake of magnitude 5.3 Mw, 5.5 ML, hit Zagreb, Croatia, with an epicenter 7 kilometres (4.3 mi) north of the city centre. The maximum felt intensity was VII–VIII (Very strong to Damaging) on the Medvedev–Sponheuer–Karnik scale. The earthquake was followed by numerous aftershocks, the strongest of which with a magnitude of 5.0. It was the strongest earthquake in Zagreb since the 1880 earthquake and caused substantial damage in the historical city center. More than 1,900 buildings were reported to have been damaged to the point of becoming uninhabitable. The earthquake was also felt in Slovenia. One person was killed and 27 others were injured.
The earthquake occurred during the coronavirus pandemic and complicated the enforcement of social distancing measures set out by the Government of Croatia. It occurred during the Croatian Presidency of the Council of the European Union.
The direct earthquake damage inflicted on Zagreb and Krapina-Zagorje County was estimated at 86 billion Croatian kuna (€11.5 billion).
[Wikipedia](https://en.wikipedia.org/wiki/2020_Zagreb_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2020                                                                   |
| Country              | Croatia                                                                |
| Region               | Zagreb                                                                 |
| Event_Name           | Zagreb_2020                                                            |
| Local_Date           | 22/03/2020                                                             |
| Local_Time           | 11:24:03                                                               |
| Latitude             | 45.9072                                                                |
| Longitude            | 15.9697                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 5.3                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 1                                                                      |
| Injured              | 27                                                                     |
| Displaced_Population | 18915                                                                  |
| Affected_Population  | 60000                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 20000 Buildings                                                        |
| Collapsed_Units      | 6350 Buildings                                                         |
| Economic_Losses      | 1800-6800 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us70008dx7/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2020_Zagreb_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
