# 🌎 1990 M7.4 Manjil-Rudbar earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1990 M7.4 Manjil-Rudbar earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The `1990 Manjil–Rudbar earthquake` occurred on Thursday, June 21, 1990 at 00:30:14 local time in northern Iran. The shock had a moment magnitude of 7.4 and a Mercalli Intensity of X (Extreme) ([Wikipedia](https://en.wikipedia.org/wiki/1990_Manjil%E2%80%93Rudbar_earthquake)). Widespread damage occurred to the northwest of the capital city of Tehran, including the cities of Rudbar and Manjil. The National Geophysical Data Center (NGDC) estimated that $8 billion in damage occurred in the affected area. Other earthquake catalogs presented estimates of the loss of life in the range of 35000–50000, with a further 60000–105000 that were injured. Moreover, there was approximately 105000–400000 displaced population.


### Type of sequence:


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
| Year                 | 1990                                                                   |
| Country              | Iran                                                                   |
| Region               | Gilan                                                                  |
| Event_Name           | Manjil-Rudbar                                                          |
| Local_Date           | 20/06/1990                                                             |
| Local_Time           | 00:30:00                                                               |
| Longitude            | 49.41                                                                  |
| Latitude             | 36.96                                                                  |
| Depth_(km)           | 18.5                                                                   |
| Mw                   | 7.4                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 13000-50000                                                            |
| Injured              | 50000-105000                                                           |
| Displaced_Population | 105000-400000                                                          |
| Affected_Population  | 70000-500000                                                           |
| Affected_Units       | 0 Units                                                                |
| Damaged_Units        | 100000-196774 Buildings                                                |
| Collapsed_Units      | 100000-321486 Buildings                                                |
| Economic_Losses      | 7000-8000 M USD                                                        |
| Insured_Losses       | 100-115 M USD                                                          |
| Induced_Effects      | Landslides, Rockfall, Tsunami                                          |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0004arq/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1990_Manjil%E2%80%93Rudbar_earthquake    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
