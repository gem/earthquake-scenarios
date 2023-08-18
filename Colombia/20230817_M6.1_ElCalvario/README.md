# 🌎 2023-08-17 M6.1 El Calvario earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2023-08-17 M6.1 El Calvario earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

A catastrophic magnitude 7.0 Mw earthquake struck Haiti at 16:53 local time (21:53 UTC) on Tuesday, 12 January 2010. The epicenter was near the town of Léogâne, Ouest department, approximately 25 kilometres (16 mi) west of Port-au-Prince, Haiti's capital.
[Wikipedia](https://en.wikipedia.org/wiki/2010_Haiti_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2023                                                                   |
| Country              | Colombia                                                               |
| Region               | Meta                                                                    |
| Event_Name           | El Calvario                                                            |
| Local_Date           | 2023-08-17                                                             |
| Local_Time           | 12:04:57                                                               |
| Longitude            | -73.5111                                                               |
| Latitude             | 4.4177                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | nan                                                                    |
| Tectonic_region_type | nan                                                                    |
| Fatalities           | 0                                                                      |
| Injured              | nan                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 82                                                                     |
| Collapsed_Units      | 10                                                                     |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us7000kp2i/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2010_Haiti_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
