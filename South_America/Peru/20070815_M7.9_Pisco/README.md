# 🌎 2007 M7.9 Pisco earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2007 M7.9 Pisco earthquake in Peru.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `2007 Pisco earthquake`, which measured 8.0 on the Mw scale, was an earthquake recorded on Wednesday, August 15, at 18:40:57 PET (23:40:57 UTC) with an approximate duration of 4 min. Its epicenter was located on the coasts of central Peru, 40 km west of Pisco and 150 km southwest of Lima, and its hypocenter was located 39 km deep. It was one of the most violent earthquakes to occur in Peru in recent years, surpassed by the 2001 Arequipa earthquake. But it was not the most catastrophic; from that point of view, the Ancash Earthquake of 1970 produced thousands of deaths. 
It left 514-600 dead, 1300-2291 injured, 48000-76000 homes totally destroyed and uninhabitable, 85000 homes affected, 431000-450000 people affected, 103 hospitals affected, and 14 hospitals destroyed according to Peruvian Government preliminary assessments. The destructive magnitude of the earthquake also caused extensive damage to the infrastructure that provides basic services to the population, such as water and sanitation, education, health, and communications. In addition, in El Carmen (Chincha), houses were completely destroyed. The region affected by this earthquake contributes 3% of the country's GDP.
The areas most affected by the earthquake correspond to the cities of the department of Ica and the province of Cañete, especially Pisco, Chincha Alta, Chincha Baja, Tambo de Mora, Ica, San Luis de Cañete, Yauyos, Huaytará, and Castrovirreyna, also affecting the capital of Peru, Lima ([Wikipedia](https://en.wikipedia.org/wiki/2007_Peru_earthquake)).


### Type of sequence
- A magnitude 5.8 aftershock occurred at 19:02 local time, centered 113 km (70 mi) northeast of Chincha Alta. At 19:19 local time, another 5.9 magnitude aftershock occurred, centered 48 km (30 mi) south-southwest of Ica. At least a dozen aftershocks of magnitude 5.0 or greater have been recorded ([Wikipedia](https://en.wikipedia.org/wiki/2007_Peru_earthquake)).


### Occurrence of other phenomena:
- A tsunami warning was issued for Peru, Ecuador, Chile, Colombia and even as far as Hawaii following the earthquakes, but was later cancelled. Some areas of the port city of Callao were evacuated. Tsunami warnings were also made for Panama and Costa Rica, and a tsunami watch was posted for Nicaragua, Guatemala, El Salvador, Mexico and Honduras. All alerts were cancelled after a 25-centimetre (10 in) wave came ashore. A tsunami did occur on the Peruvian coast. It flooded part of Lima's Costa Verde highway, and much of Pisco's shore. It has been reported that the tsunami reached as high as 5 m (16 ft) in the zone of Lagunillas in Pisco neighbourhood's town Paracas, with a maximum height of 10.05 m (33.0 ft) in Yumaque. The fishing village of Lagunilla completely destroyed by the tsunami resulting in 3 deaths out of 7 inhabitants, while survivors reported no significant earthquake damage. The Japan Meteorological Agency issued a tsunami warning, projecting that waves higher than 20 cm could reach Japan's northern island, Hokkaidō, on Thursday, August 16, around 19:00 UTC. Following image shows an animation of the tsunami caused by this earthquake ([Wikipedia](https://en.wikipedia.org/wiki/2007_Peru_earthquake)).

<img src="https://www.data.jma.go.jp/svd/eqev/data/tsunami/peru_20070816.gif"  width="550" height="400"> 

Figure Source: [JMA](https://www.data.jma.go.jp/svd/eqev/data/tsunami/generation.html)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2007                                                                   |
| Country              | Peru                                                                   |
| Region               | Pisco                                                                  |
| Event_Name           | Pisco_2007                                                             |
| Local_Date           | 15/08/2007                                                             |
| Local_Time           | 18:40:58                                                               |
| Latitude             | -13.67                                                                 |
| Longitude            | -76.76                                                                 |
| Depth_(km)           | 40                                                                     |
| Mw                   | 7.9                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse Fault                                                          |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | 337-610                                                                |
| Injured              | 1042-2291                                                              |
| Displaced_Population | 100000                                                                 |
| Affected_Population  | 32000-722643                                                           |
| Affected_Units       | 2574-13688 Units                                                       |
| Damaged_Units        | 17000-230000 Units                                                     |
| Collapsed_Units      | 33676-94000 Units                                                      |
| Economic_Losses      | 139.1-600 M USD                                                        |
| Insured_Losses       | 200 M USD                                                              |
| Induced_Effects      | Tsunami, Landslides, Liquefaction                                      |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000fjta/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2007_Peru_earthquake                     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
