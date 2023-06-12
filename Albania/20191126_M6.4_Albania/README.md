# 🌎 2019 M6.4 Durres earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2019 M6.4 Durres earthquake in Albania.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

Northwestern Albania was struck by a magnitude 6.4 earthquake with an epicentre 16 kilometres (9.9 mi) west-southwest of Mamurras, at 03:54 CET (UTC+1) on 26 November 2019. The earthquake lasted at least 50 seconds and was felt in Albania's capital Tirana, and in places as far away as Bari, Taranto and Belgrade, 370 kilometres (230 mi) northeast of the epicentre. The maximum felt intensity was VIII (Severe) on the Modified Mercalli intensity scale. A total of 51 people were killed in the earthquake, with about 3,000 injured. It was the second earthquake to strike the region in the space of three months. It was the strongest earthquake to hit Albania in more than 40 years, its deadliest earthquake in 99 years and the world's deadliest earthquake in 2019.
[Wikipedia](https://en.wikipedia.org/wiki/2019_Albania_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2019                                                                   |
| Country              | Albania                                                                |
| Region               | Durres                                                                 |
| Event_Name           | Durres                                                                 |
| Local_Date           | 26/11/2019                                                             |
| Local_Time           | 02:54:12                                                               |
| Latitude             | 41.5138                                                                |
| Longitude            | 19.5256                                                                |
| Depth_(km)           | 22                                                                     |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 51                                                                     |
| Injured              | 913-2000                                                               |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 202913                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 83000 Buildings                                                        |
| Collapsed_Units      | 11000 Buildings                                                        |
| Economic_Losses      | 700-1081 M USD                                                         |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us70006d0m/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2019_Albania_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
