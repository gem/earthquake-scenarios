# 🌎 2016 M6.6 CentralItaly earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2016 M6.6 CentralItaly earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

A series of major earthquakes struck Central Italy between the Marche and Umbria regions in October 2016. The third quake on 30 October was the largest in Italy in 36 years, since the 1980 Irpinia earthquake.
[Wikipedia](https://en.wikipedia.org/wiki/October_2016_Central_Italy_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2016                                                                   |
| Country              | Italy                                                                  |
| Region               | Umbria, Lazio, Abruzzo and Marche                                      |
| Event_Name           | CentralItaly                                                           |
| Local_Date           | 24/08/2016                                                             |
| Local_Time           | 01:36:32                                                               |
| Latitude             | 42.723                                                                 |
| Longitude            | 13.1877                                                                |
| Depth_(km)           | 4.44                                                                   |
| Mw                   | 6.6                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 325-336                                                                |
| Injured              | 379-455                                                                |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 30184                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 5418 M USD                                                             |
| Insured_Losses       | 81 M USD                                                               |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10006g7d/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/August_2016_Central_Italy_earthquake     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
