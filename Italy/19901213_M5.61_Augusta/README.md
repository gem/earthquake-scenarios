# 🌎 1990 M5.6 Augusta earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1990 M5.6 Augusta earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1990 Carlentini earthquake (Italian: Terremoto di Carlentini del 1990) occurred off the Sicilian coast, 20 km east northeast from the town of Augusta, Sicily on 13 December at 01:24 local time. The moderately-sized earthquake measuring 5.6 on the moment magnitude scale (Mw ) resulted in the deaths of 19 people and caused at least 200 injuries. It also inflicted significant damage in the region, leaving 2,500 homeless.
Lasting 45 seconds, the shock was assigned a maximum Modified Mercalli intensity of VII–VIII (Very strong–Severe). The earthquake was followed-up by four aftershocks that were felt by people.
[Wikipedia](https://en.wikipedia.org/wiki/1990_Carlentini_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1990                                                                   |
| Country              | Italy                                                                  |
| Region               | Augusta                                                                |
| Event_Name           | Augusta_1990                                                           |
| Local_Date           | 13/12/1990                                                             |
| Local_Time           | 00:24:25                                                               |
| Latitude             | 37.3                                                                   |
| Longitude            | 15.438                                                                 |
| Depth_(km)           | 11.1                                                                   |
| Mw                   | 5.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 17-19                                                                  |
| Injured              | 200-300                                                                |
| Displaced_Population | 2500-15000                                                             |
| Affected_Population  | 2700-15152                                                             |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 6103-7104 Buildings                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 115-500 M USD                                                          |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0004j1w/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1990_Carlentini_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
