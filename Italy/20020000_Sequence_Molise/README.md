# 🌎 2002 M5.9 Molise earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2002 M5.9 Molise earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

Two earthquakes hit the Italian regions of Molise and Apulia on 31 October at 10:32:58 (UTC) and 1 November at 15:09:00 (UTC). The shocks had magnitudes of 5.9 and 5.8 Mw respectively. Most of the victims were killed and injured when a school collapsed in the town of San Giuliano di Puglia:  26 of the 51 schoolchildren died, together with one of their teachers. In particular, none of the nine children in the school's 4th Year (mostly born in 1996) survived.
[Wikipedia](https://en.wikipedia.org/wiki/2002_Molise_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2002                                                                   |
| Country              | Italy                                                                  |
| Region               | Molise                                                                 |
| Event_Name           | Molise_2002                                                            |
| Local_Date           | 31/10/2002                                                             |
| Local_Time           | 10:32:58                                                               |
| Latitude             | 41.789                                                                 |
| Longitude            | 14.872                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 5.9                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 29-30                                                                  |
| Injured              | 33-135                                                                 |
| Displaced_Population | 2295-3000                                                              |
| Affected_Population  | 8533                                                                   |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 796 M USD                                                              |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000bfqg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2002_Molise_earthquakes                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
