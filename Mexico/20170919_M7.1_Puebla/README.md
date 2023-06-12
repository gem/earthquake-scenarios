# 🌎 2017 M7.1 Puebla earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M7.1 Puebla earthquake in Mexico.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2017 Puebla earthquake` struck at 13:14 CDT (18:14 UTC) on 19 September 2017 with an estimated magnitude of Mw7.1 and strong shaking for about 20 seconds. Its epicenter was about 55 km (34 mi) south of the city of Puebla, Mexico. The earthquake caused damage in the Greater Mexico City area and 7 states (with the largest impact in Morelos and Puebla), including the collapse of more than 59 buildings. 369 people were killed by the earthquake due to collapsed buildings, including 228 in Mexico City, and more than 6,000 people were injured. Multiple facilities in Mexico city were disrrupted by the event, such as the international airport, the highway between Mexico and Acapulco and other important roads were affected.
[Wikipedia](https://en.wikipedia.org/wiki/2017_Puebla_earthquake)

Many of the collapsed buildings in Mexico City were mid-rise reinforced concrete with masonry infills. High controversy arose in the community due to the lack of building code enforcement in relatevly modern construction or retrofitted buildings (GEER_2017).
From the collapsed structures, a 7‐story office building in Mexico city was the cause of 47 casualties and several injuries (GEER_2017).


### Type of sequence
- While the Mw7.1 Puebla earthquake comes only 11 days after the Mw8.1 earthquake that occurred 650 km to the southeast (and both events were related to the subduction of the Cocos plate beneath the North American plate), the Mw7.1 event occurred too far north along the subduction zone to be an aftershock of the September 7, 2017, earthquake according to the USGS.[Verisk](https://www.air-worldwide.com/news-and-events/press-releases/air-worldwide-estimates-insured-losses-from-september-19-central-mexico-m7-1-earthquake/)
- Aftershocks until 12:30 p.m. on 09/23/2017: 39 [Tweet_Spanish](https://twitter.com/SismologicoMX/status/911669047015636992) 
- Aftershocks until 09/23/2017 from [Wikipedia](https://en.wikipedia.org/wiki/2017_Puebla_earthquake)

<img src="/Mexico/20170919_M7.1_Puebla/References/2017_Central_Mexico_earthquake_aftershocks_SSN.png"  width="550" height="400">

Figure source: [Wikipedia](https://en.wikipedia.org/wiki/2017_Puebla_earthquake)


### Occurrence of other phenomena: 
- The occurance of 12 landslides were quantified in the Puebla state. [NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-more-info/10267)
- Overall, the consequences of slope instabilities caused by the 2017 Puebla-Mexico City earthquake were relatively minor compared with the reported structural damage. More than 360 deaths were attributed to this earthquake of which one death was attributed to landslide activities. The size of the area affected by landslides and the intensity of shaking in these areas was consistent with relationships developed in previous studies. The lack of major effects from earthquake-induced landslides is consistent with previous earthquakes in central and southern Mexico and stands in sharp contrast to many parts of Central America where earthquake-induced landslides pose a significant hazard.[Montgomery et al. 2020](https://www.sciencedirect.com/science/article/pii/S0267726119309078?via%3Dihub)
- [GEER_2017](https://geerassociation.org/component/geer_reports/?view=geerreports&id=82&layout=build) provides additional information on Slope Instability, Lifelines and Critical Infrastructure.


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
| Country              | Mexico                                                                 |
| Region               | Puebla                                                                 |
| Event_Name           | Puebla_2017                                                            |
| Local_Date           | 19/09/2017                                                             |
| Local_Time           | 13:14:39                                                               |
| Latitude             | 18.3297                                                                |
| Longitude            | -98.6712                                                               |
| Depth_(km)           | 51.2                                                                   |
| Mw                   | 7.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 362-471                                                                |
| Injured              | 6000-7289                                                              |
| Displaced_Population | 5000-193546                                                            |
| Affected_Population  | 216672-250000                                                           |
| Affected_Units       | 150000-190000 Buildings                                                     |
| Damaged_Units        | 54473 Buildings                                                     |
| Collapsed_Units      | 19261 Buildings                                                        |
| Economic_Losses      | 4000-8000 M USD                                                        |
| Insured_Losses       | 725-2000 M USD                                                         |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us2000ar20/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2017_Puebla_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
