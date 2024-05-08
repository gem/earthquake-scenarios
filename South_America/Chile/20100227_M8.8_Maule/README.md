# 🌎 2010 M8.8 Maule earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2010 M8.8 Maule earthquake in Chile.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `2010 Chilean earthquake and tsunami (known by the number 27F)` was an earthquake that occurred at 03:34:08 local time (UTC–3) on Saturday, February 27, 2010, that reached a magnitude of Mw8.8. The earthquake was reported as sensitive between the cities of Calama (Antofagasta Region) and Puerto Montt (Los Lagos Region), registering a maximum intensity of IX on the Modified Mercalli scale in the Bío Bío Region. The affected regions were Valparaíso, Metropolitana de Santiago, O'Higgins, Maule, and Biobío, which accumulate more than 13 million inhabitants, about 80% of the country's population. In the Maule and Biobío regions devastating an important part of cities such as Constitución, Concepción, Pelluhue, Curanipe, Iloca, Cobquecura and the port of Talcahuano. Much of the center of the cities of Curicó and Talca collapsed, and the old buildings of its historic center were destroyed in their entirety. In the regions of La Araucanía, O'Higgins and Metropolitana causing destruction in Santiago, Rancagua, and in rural localities, power cuts in Concepción and Santiago. Tremors were felt in many Argentine cities, including Buenos Aires, Córdoba, Mendoza, and La Rioja. Tremors were felt as far north as the city of Ica in southern Peru (approx. 2,400 km (1,500 mi) away). The fatalities reached 525 deaths. The earthquake left 23-25 missing. Nearly 500000 homes are destroried and at least 1500000 damaged to some extent. 2000000 people are estimated to have been affected by the worst natural tragedy experienced in Chile since 1960. The total economic loss in Chile was estimated at 30 billion USD (More detailed information regarding Estimated loss based on sectors can be found in OPS_Report_2010.pdf in the Reference folder). ([CSN](https://www.csn.uchile.cl/efemerides-sismicas-terremoto-del-maule-2010/) and [Wikipedia](https://en.wikipedia.org/wiki/2010_Chile_earthquake)).
- This earthquake occurred between the ruptures activated by the earthquakes of May 1960 (19600522_M9.5_Valdivia) in the south and the Valparaíso earthquake of 1985 in the north. This area remained in a seismic silence for more than 170 years since the subduction of the Nazca plate under the South American was all that period without releasing energy through seismic events of great magnitude. Therefore, already in 2009, seismologists indicated the possibility of a large earthquake in that area ([CSN](https://www.csn.uchile.cl/efemerides-sismicas-terremoto-del-maule-2010/)). 


### Type of sequence
- During the first three months of the event, more than 283 aftershocks with magnitude greater than 5.0 were recorded, and 22 with magnitude equal to or greater than 6.0. Several thousand aftershocks of smaller magnitude were recorded, generally not felt by the population. On March 11 at 11:39 and 11:55 (local time) two earthquakes of magnitude close to 7 occurred in the vicinity of Pichilemu. These replicas were among the largest of the recorded sequence. The events, located at geographical coordinates 34.26°S, 71.88°W and 34.301°S, 72.13°W, at shallow depths, did not occur along the contact plane between the Nazca and South American plates, the plane in which the fault that originated the earthquake of February 27 was activated, but were located inside the riding plate, that is, on the South American plate. However, the earthquakes of March 11 can be considered as triggered aftershocks, since it is most likely that they would not have occurred if the fault associated with the February 27 event was not previously activated ([CSN](https://www.csn.uchile.cl/efemerides-sismicas-terremoto-del-maule-2010/)). For more information about aftershocks check Wikipedia ([English](https://en.wikipedia.org/wiki/2010_Chile_earthquake) and [Spanish](https://es.wikipedia.org/wiki/Terremoto_de_Chile_de_2010)).


### Occurrence of other phenomena: 
- A tsunami warning was first declared for Chile and Peru, and a tsunami watch for Ecuador, Colombia, Antarctica, Panama and Costa Rica. The warning was later extended to a Pacific Ocean-wide warning, covering all coastal areas on the Pacific Ocean except the west coast of the United States, British Columbia, and Alaska.  Although the earthquake killed far fewer people than the Haitian earthquake less than 7 weeks prior, it was still devastating. The tsunami warning was cancelled for all countries except Japan and Russia. In Chile, consecutive tsunamis hit coastal towns, among which Constitución suffered the hardest damage; subsequently, a tsunami amplitude of up to 2.6 m high was recorded in the sea at Valparaíso. A wave amplitude of 2.34 m was recorded at Talcahuano in the Biobío Region. Robinson Crusoe Island, the largest of the Juan Fernández Islands, was struck by a large wave which led to the deaths of four people on the island, with eleven people reported as missing, according to Provincial Governor Ivan De La Maza. For more information about tsunami check Wikipedia ([English](https://en.wikipedia.org/wiki/2010_Chile_earthquake) and [Spanish](https://es.wikipedia.org/wiki/Terremoto_de_Chile_de_2010)). The number of deaths due to those homes severely damaged by the tsunami has been mentioned in Contreras_and_Winckler_2013.pdf in the Reference folder.

<img src="Chile/20100227_M8.8_Maule/References/Tsunami_Image.jpg"  width="400" height="450">

Figure source: [NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-more-info/4682)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                                              |
|:---------------------|:-----------------------------------------------------------------------------------------|
| Year                 | 2010                                                                                     |
| Country              | Chile                                                                                    |
| Region               | Maule                                                                                    |
| Event_Name           | Maule_2010                                                                               |
| Local_Date           | 27/02/2010                                                                               |
| Local_Time           | 03:34:00                                                                                 |
| Latitude             | -36.1723                                                                                 |
| Longitude            | -73.142                                                                                  |
| Depth_(km)           | 30                                                                                       |
| Mw                   | 8.8                                                                                      |
| Max_Intensity_(MMI)  | VIII                                                                                     |
| Fault_mechanism      | Reverse                                                                                  |
| Tectonic_region_type | Subduction                                                                               |
| Fatalities           | 486-562                                                                                  |
| Injured              | 500-12000                                                                                |
| Displaced_Population | 800000-2000000                                                                           |
| Affected_Population  | 800000-1861222                                                                           |
| Affected_Units       | 1500000 Units                                                                            |
| Damaged_Units        | 126883-500000 Units                                                                      |
| Collapsed_Units      | 81444-81449 Units                                                                        |
| Economic_Losses      | 15000-37280 M USD                                                                        |
| Insured_Losses       | 4000-9941 M USD                                                                          |
| Induced_Effects      | Tsunami, Landslides                                                                      |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/official20100227063411530_30/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2010_Chile_earthquake                                      |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
