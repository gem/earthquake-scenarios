# 🌎 1989 M5.4 Newcastle earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1989 M5.4 Newcastle earthquake in Australia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1989 Newcastle earthquake was an intraplate earthquake that occurred in Newcastle, New South Wales on Thursday 28 December. The shock measured 5.6 on the Richter magnitude scale and was one of Australia's most serious natural disasters, killing 13 people and injuring more than 160. The damage bill has been estimated at A$4 billion (or $8.5 billion in 2018, adjusted for inflation), including an insured loss of about $1 billion (or $2.1 billion in 2018, adjusted for inflation).The effects were felt over an area of around 200,000 square kilometres (77,000 sq mi) in the state of New South Wales, with isolated reports of movement in areas up to 800 kilometres (500 mi) from Newcastle. Damage to buildings and facilities was reported over an area of 9,000 km2 (3,500 sq mi).
[Wikipedia](https://en.wikipedia.org/wiki/1989_Newcastle_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1989                                                                   |
| Country              | Australia                                                              |
| Region               | Newcastle                                                              |
| Event_Name           | Newcastle                                                              |
| Local_Date           | 28/12/1989                                                             |
| Local_Time           | 10:27:00                                                               |
| Longitude            | 151.619                                                                |
| Latitude             | -32.967                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 5.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Thrust/reverse                                                         |
| Tectonic_region_type | Stable Continental Regions (SCRs)                                      |
| Fatalities           | 9-12                                                                   |
| Injured              | 100-160                                                                |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 2000-300000                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 1000-50000                                                             |
| Collapsed_Units      | 300                                                                    |
| Economic_Losses      | 900-1100 M                                                             |
| Insured_Losses       | 396-500 M                                                              |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp00043na/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1989_Newcastle_earthquake                |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
