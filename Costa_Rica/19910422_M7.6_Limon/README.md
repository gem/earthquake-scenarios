# 🌎 1991 M7.6 Limon earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1991 M7.6 Limon earthquake in Costa_Rica.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `1991 Costa Rica earthquake`, also known as the `Limon` earthquake or Bocas del Toro earthquake, occurred at 3:57 pm local time (21:56:51 UTC) on April 22. The epicenter of the 7.7 Mw earthquake was in Pandora, Valle La Estrella, in the Caribbean region of Limon, Costa Rica, 225 kilometres (140 mi) southeast of San José. The earthquake was the strongest recorded in Costa Rica's history, and was felt throughout the country as well as in western Panama. ([Wikipedia](https://en.wikipedia.org/wiki/1991_Limon_earthquake)). 


### Type of sequence



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
| Year                 | 1991                                                                   |
| Country              | Costa Rica                                                             |
| Region               | Limon                                                                  |
| Event_Name           | Limon                                                                  |
| Local_Date           | 22/04/1991                                                             |
| Local_Time           | 15:57:00                                                               |
| Longitude            | -83.073                                                                |
| Latitude             | 9.685                                                                  |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Shallow crustal                                                        |
| Fatalities           | 47-127                                                                 |
| Injured              | 109-895                                                                |
| Displaced_Population | 7439-10900                                                             |
| Affected_Population  | 6320                                                                   |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 7869 Buildings                                                         |
| Collapsed_Units      | 4452 Buildings                                                         |
| Economic_Losses      | 43-510 M USD                                                           |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Tsunami, landslides, liquefaction                                      |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0004qpg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1991_Limon_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
