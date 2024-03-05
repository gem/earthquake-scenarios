# 🌎 1999 M6 Athens earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1999 M6 Athens earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1999 Athens earthquake occurred on September 7 at 14:56:51 local time near Mount Parnitha in Greece with a moment magnitude of 6.0 and a maximum Mercalli intensity of IX (Violent). The proximity to the Athens metropolitan area resulted in widespread structural damage, mainly to the nearby suburbs of Ano Liossia, Acharnes, Fyli, Thrakomakedones, Kifissia, Metamorfosi, Kamatero and Nea Philadelphia. More than 100 buildings (including three major factories) across those areas collapsed trapping scores of victims under their rubble while dozens more were severely damaged. With damage estimated at $3–4.2 billion, 143 people were killed, and up to 1,600 were treated for injuries in Greece's deadliest natural disaster in almost half a century.
[Wikipedia](https://en.wikipedia.org/wiki/1999_Athens_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1999                                                                   |
| Country              | Greece                                                                 |
| Region               | Athens                                                                 |
| Event_Name           | Athens_1999                                                            |
| Local_Date           | 07/09/1999                                                             |
| Local_Time           | 11:56:49                                                               |
| Latitude             | 38.119                                                                 |
| Longitude            | 23.605                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6                                                                      |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 143                                                                    |
| Injured              | 750-2000                                                               |
| Displaced_Population | 108                                                                    |
| Affected_Population  | 113031                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 53000 Buildings                                                        |
| Economic_Losses      | 4200 M USD                                                             |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0009e46/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1999_Athens_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
