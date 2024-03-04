# 🌎 1999 M7.6 Izmit earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1999 M7.6 Izmit earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On the 17th of August, 1999 at 3:01 AM local time, a catastrophic magnitude 7.6 earthquake struck the Kocaeli Province of Turkey, causing monumental damage and 17,127–18,373 deaths. Named for the quakes proximity to the northeastern city of Izmit, the earthquake is also commonly referred to as the August 17 Earthquake or the 1999 Gölcük Earthquake. The earthquake occurred on 00:01 UTC at a shallow depth of 15 km. A maximum Mercalli intensity of X (Extreme) was observed, marking this event as one of the most destructive earthquakes in the history of the region. The earthquake lasted for 37 seconds, causing seismic damage and becoming widely remembered as one of the deadliest natural disasters in modern Turkish history.
The 1999 earthquake was part of a sequence along the North Anatolian Fault that started in 1939, causing large earthquakes that moved progressively from east to west over a period of 60 years.
[Wikipedia](https://en.wikipedia.org/wiki/1999_%C4%B0zmit_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1999                                                                   |
| Country              | Turkey                                                                 |
| Region               | Izmit                                                                  |
| Event_Name           | Izmit                                                                  |
| Local_Date           | 17/08/1999                                                             |
| Local_Time           | 00:01:39                                                               |
| Latitude             | 40.748                                                                 |
| Longitude            | 29.864                                                                 |
| Depth_(km)           | 17                                                                     |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | X                                                                      |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 17118-18373                                                            |
| Injured              | 43953-50000                                                            |
| Displaced_Population | 600000                                                                 |
| Affected_Population  | 1358953                                                                |
| Affected_Units       | 241000 Buildings                                                       |
| Damaged_Units        | 73342-108000 Buildings                                                 |
| Collapsed_Units      | 16400 Buildings                                                        |
| Economic_Losses      | 20000-30000 M USD                                                      |
| Insured_Losses       | 2000 M USD                                                             |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0009d4z/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1999_%C4%B0zmit_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
