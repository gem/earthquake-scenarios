# 🌎 1978 M7.3 Tabas earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1978 M7.3 Tabas earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The `1978 Tabas earthquake` occurred on September 16 at 19:05:55 local time in central Iran. The shock measured 7.4 on the moment magnitude scale and had a MMI of IX+ (Violent). The death toll was in the range of 15000–25000, with severe damage occurring in the town of Tabas.
Eighty percent of the human deaths occurred in Tabas, but a total of 85 villages were also affected. This seismic force was felt in Tehran, about 610 kilometers (380 mi) away. About 55–85 km (34–53 mi) of ground deformation was observed, with about 1.7 meters (5 ft 7 in) of maximum slip ([Wikipedia](https://en.wikipedia.org/wiki/1978_Tabas_earthquake)).


### Type of sequence:
- Only one significant M5 aftershock occurred ([Wikipedia](https://en.wikipedia.org/wiki/1978_Tabas_earthquake)).


### Occurrence of other phenomena: 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1978                                                                   |
| Country              | Iran                                                                   |
| Region               | Yazd                                                                   |
| Event_Name           | Tabas                                                                  |
| Local_Date           | 16/09/1978                                                             |
| Local_Time           | 19:06:00                                                               |
| Longitude            | 57.44                                                                  |
| Latitude             | 33.37                                                                  |
| Depth_(km)           | 33                                                                     |
| Mw                   | 7.3                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Thrust                                                                 |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 14800-25000                                                            |
| Injured              | 6400                                                                   |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 40000-53994                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 15000 Buildings                                                        |
| Economic_Losses      | 11-50 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0000wjx/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1978_Tabas_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
