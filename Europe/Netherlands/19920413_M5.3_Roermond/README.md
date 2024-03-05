# 🌎 1992 M5.4 Roermond earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1992 M5.4 Roermond earthquake in Netherlands.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1992 Roermond earthquake occurred on 13 April, around 3:20 AM (1:20 UTC) with a moment magnitude of 5.3 and a maximum Mercalli intensity of VIII (Severe). Striking on the Peel Boundary Fault, a normal fault near Roermond, it was the strongest recorded earthquake in the Netherlands and in Northwestern Europe, and caused substantial damage to older buildings in the Netherlands and adjacent countries of Belgium and Germany. A series of aftershocks followed.
[Wikipedia](https://en.wikipedia.org/wiki/1992_Roermond_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1992                                                                   |
| Country              | Netherlands                                                            |
| Region               | Roermond                                                               |
| Event_Name           | Roermond_1992                                                          |
| Local_Date           | 13/04/1992                                                             |
| Local_Time           | 01:20:00                                                               |
| Latitude             | 51.153                                                                 |
| Longitude            | 5.798                                                                  |
| Depth_(km)           | 21.2                                                                   |
| Mw                   | 5.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Stable Continental                                                     |
| Fatalities           | nan                                                                    |
| Injured              | 20-45                                                                  |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 1500                                                                   |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 50-100 M USD                                                           |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp00055q3/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1992_Roermond_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
