# 🌎 2020 M6.4 Petrijna earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2020 M6.4 Petrijna earthquake in Croatia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

At approximately 12:20 PM CET (11:20 UTC) on 29 December 2020, an earthquake of magnitude 6.4 Mw (6.2 ML) hit central Croatia, with an epicenter located roughly 3 km (1.9 mi) west-southwest of Petrinja. The maximum felt intensity was estimated at VIII (Heavily damaging) to IX (Destructive) on the European macroseismic scale. Before this event there were three foreshocks, the strongest of which had a magnitude of 5.2 Mw on the day before. The earthquake was followed by numerous aftershocks, the strongest of which had a magnitude of 4.9 Mw. The adversely affected areas were mostly in the Sisak-Moslavina County and other nearby Croatian counties, as well as some of the nearby areas of Bosnia and Slovenia.
Seven people were confirmed dead, while 26 others were injured, with six having serious injuries. Initial reports show many buildings destroyed in Petrinja. The mayor of Petrinja, Darinko Dumbović, said that half of the town has been destroyed.The first multidisciplinary scientific paper on Petrinja 2020 earthquake was published in Remote Sensing journal in March 2021.
[Wikipedia](https://en.wikipedia.org/wiki/2020_Petrinja_earthquake)



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
| Region               | Petrijna                                                               |
| Event_Name           | Petrijna_2020                                                          |
| Local_Date           | 29/12/2020                                                             |
| Local_Time           | 18:19:54                                                               |
| Latitude             | 45.4244                                                                |
| Longitude            | 16.2573                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 8                                                                      |
| Injured              | 36                                                                     |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 149407                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 34056-46000 Buildings                                                  |
| Collapsed_Units      | 1500-3062 Buildings                                                    |
| Economic_Losses      | 4187-6223 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us6000d3zh/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2020_Petrinja_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
