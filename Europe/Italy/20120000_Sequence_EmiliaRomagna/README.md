# 🌎 2012 M6 EmiliaRomagna earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2012 M6 EmiliaRomagna earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

In May 2012, two major earthquakes struck Northern Italy, causing 27 deaths and widespread damage. The events are known in Italy as the 2012 Emilia earthquakes, because they mainly affected the Emilia region.
The first earthquake, registering magnitude 6.1, struck in the Emilia-Romagna region, about 36 kilometres (22 miles) north of the city of Bologna, on 20 May at 04:03 local time (02:03 UTC). The epicentre was between Finale Emilia, Bondeno and Sermide. Two aftershocks of magnitude 5.2 occurred, one approximately an hour after the main event and another approximately eleven hours after the main event. Seven people were killed.
A magnitude 5.8 earthquake struck the same area nine days later, on 29 May, causing an additional twenty deaths and widespread damage, particularly to buildings already weakened by the 20 May earthquake. The epicentre was in Medolla: the quake itself occurred at a depth of about 10 kilometres (6.2 mi)
[Wikipedia](https://en.wikipedia.org/wiki/2012_Northern_Italy_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2012                                                                   |
| Country              | Italy                                                                  |
| Region               | EmiliaRomagna                                                          |
| Event_Name           | EmiliaRomagna_2012                                                     |
| Local_Date           | 20/05/2012                                                             |
| Local_Time           | 02:03:52                                                               |
| Latitude             | 44.89                                                                  |
| Longitude            | 11.23                                                                  |
| Depth_(km)           | 6.3                                                                    |
| Mw                   | 6                                                                      |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Inverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 7-26                                                                   |
| Injured              | 50-350                                                                 |
| Displaced_Population | 15000                                                                  |
| Affected_Population  | 11050-15000                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 10000 M EUR -15800 M USD                                               |
| Insured_Losses       | 1300 M USD                                                             |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000jkn8/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2012_Northern_Italy_earthquakes          |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
