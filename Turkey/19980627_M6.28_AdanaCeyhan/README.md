# 🌎 1998 M6.3 AdanaCeyhan earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1998 M6.3 AdanaCeyhan earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1998 Adana–Ceyhan earthquake occurred at 16:55 local time on 27 June with a moment magnitude of 6.3 and a maximum intensity of IX (Destructive) on the European macroseismic scale. The total economic loss was estimated at about US$1 billion.
The event occurred in Cilicia region in southern Turkey and killed at least 145 people and left 1,500 people wounded and many thousands homeless in Adana, and Ceyhan, the most populous town of the Adana Province, as well as many villages located between both cities along the Ceyhan River. The most casualties and damage occurred due to inadequately engineered buildings in the town of Ceyhan.
[Wikipedia](https://en.wikipedia.org/wiki/1998_Adana%E2%80%93Ceyhan_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1998                                                                   |
| Country              | Turkey                                                                 |
| Region               | AdanaCeyhan                                                            |
| Event_Name           | AdanaCeyhan_1998                                                       |
| Local_Date           | 27/06/1998                                                             |
| Local_Time           | 16:55:52                                                               |
| Latitude             | 36.878                                                                 |
| Longitude            | 35.307                                                                 |
| Depth_(km)           | 33                                                                     |
| Mw                   | 6.3                                                                    |
| Max_Intensity_(MMI)  | IV                                                                     |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 145                                                                    |
| Injured              | 1500-1600                                                              |
| Displaced_Population | 88000                                                                  |
| Affected_Population  | 1500000                                                                |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 1700 Buildings                                                         |
| Economic_Losses      | 550-1300 M USD                                                         |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0008qkc/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1998_Adana%E2%80%93Ceyhan_earthquake     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
