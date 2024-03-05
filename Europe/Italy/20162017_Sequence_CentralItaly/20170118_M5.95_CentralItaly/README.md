# 🌎 2017 M5.7 CentralItaly earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M5.7 CentralItaly earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

A series of four major earthquakes struck Central Italy between Abruzzo, Lazio, the Marche and Umbria regions on 18 January 2017.
[Wikipedia](https://en.wikipedia.org/wiki/January_2017_Central_Italy_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2017                                                                   |
| Country              | Italy                                                                  |
| Region               | CentralItaly                                                           |
| Event_Name           | CentralItaly_2017                                                      |
| Local_Date           | 18/01/2017                                                             |
| Local_Time           | 10:14:10                                                               |
| Latitude             | 42.6012                                                                |
| Longitude            | 13.2268                                                                |
| Depth_(km)           | 7                                                                      |
| Mw                   | 5.7                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 29-34                                                                  |
| Injured              | 11                                                                     |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 11                                                                     |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 18 M USD                                                               |
| Insured_Losses       | 6 M USD                                                                |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10007twj/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/January_2017_Central_Italy_earthquakes   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
