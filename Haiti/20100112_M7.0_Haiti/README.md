# 🌎 2010 M7 Haiti earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2010 M7 Haiti earthquake in Haiti.

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
| Year                 | 2010                                                                   |
| Country              | Haiti                                                                  |
| Region               | Port-au-Prince                                                         |
| Event_Name           | Haiti                                                                  |
| Local_Date           | 01/12/2010                                                             |
| Local_Time           | 16:53:10                                                               |
| Longitude            | -72.571                                                                |
| Latitude             | 18.443                                                                 |
| Depth_(km)           | 13                                                                     |
| Mw                   | 7                                                                      |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 158679-316000                                                          |
| Injured              | 300000                                                                 |
| Displaced_Population | 1269110-1800000                                                        |
| Affected_Population  | 3000000-3700000                                                        |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 285677-317289                                                          |
| Collapsed_Units      | 105000-188383                                                          |
| Economic_Losses      | 7000-8000 M USD                                                        |
| Insured_Losses       | 200 M USD                                                              |
| Induced_Effects      | Liquefaction                                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000h60h/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2010_Haiti_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
