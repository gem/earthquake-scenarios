# 🌎 1960 M9.5 Valdivia earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1960 M9.5 Valdivia earthquake in Chile.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1960 Valdivia earthquake and tsunami` or the Great Chilean earthquake on 22 May 1960 was the most powerful earthquake ever recorded. Various studies have placed it at 9.4–9.6 on the moment magnitude scale. It occurred in the afternoon (19:11 GMT, 15:11 local time), and lasted for approximately 10 minutes. The resulting tsunamis affected southern Chile, Hawaii, Japan, the Philippines, eastern New Zealand, southeast Australia, and the Aleutian Islands. The epicenter of this megathrust earthquake was near Lumaco, approximately 570 kilometers (350 mi) south of Santiago, with Valdivia being the most affected city ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)).


### Type of sequence
- The sequence of earthquakes begins with a precursor earthquake on May 21 at 06:02 UTC in the Arauco Peninsula, which reached a magnitude Mw 8.1, followed by another seismic event of magnitude 7.8, which occurred in the same area just 15 minutes before the Valdivia megaearthquake ([CSN](https://www.csn.uchile.cl/efemerides-sismicas-gran-terremoto-de-valdivia-de-1960/)).
- One of the main aftershocks occurred on 6 June in Aysén Region. This earthquake probably occurred along the Liquiñe-Ofqui Fault, meaning in this case that the fault would have moved as a consequence of the 22 May Valdivia earthquake ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)).


### Occurrence of other phenomena:
- The massive earth movement triggered a number of natural disasters in addition to **tsunamis**, including **landslides**, a **flood**, and a **volcanic eruption**, as well as a **seiche** on an Argentina lake more than 124 miles away from the epicenter. 
- **Landslides** did not cause many fatalities nor significant economic losses because most of the areas were uninhabited, with only minor roads. One landslide caused destruction and alarm following its blockage of the outflow of Riñihue Lake. The Golgol landslides destroyed parts of international Route 215-CH, which connects to Bariloche in Argentina through Cardenal Antonio Samoré Pass. ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)).
- A **Seiche** of more than 1 meter was observed on Panguipulli Lake following the earthquake. On 22 May, a seiche occurred also in Nahuel Huapi Lake, on the Argentine side of the Andes, more than 200 km away from Valdivia. The wave, most likely produced by an earthquake-triggered sediment slide at the lake bottom, killed two people and destroyed a pier in San Carlos de Bariloche city ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)).
- On 24 May, 38 hours after the main shock of the 1960 Valdivia earthquake, the Cordón Caulle **Volcano erupted**. The eruption was believed to have been triggered by the earthquake. As a result of an evacuation plan, there were no reported human deaths associated with the eruption ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)).
- Earthquake-induced **Tsunamis** affected southern Chile, Hawaii, Japan, the Philippines, China, eastern New Zealand, southeast Australia, and the Aleutian Islands. Some localized tsunamis severely battered the Chilean coast, with waves up to 25 m (82 ft). The main tsunami crossed the Pacific Ocean at a speed of several hundred km/h and devastated Hilo, Hawaii, killing 61 people. Most of the tsunami-related deaths in Japan occurred in the northeast Sanriku region of Honshu ([Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake); For more information about Tsunami Impacts in Hawaii, Japan, the Philippines and the United States refer to [USGS](https://earthquake.usgs.gov/earthquakes/eventpage/official19600522191120_30/impact)).
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Tsunami_travel_time_Valdivia_1960.jpg"  width="350" height="350">

Figure source: [Wikipedia](https://en.wikipedia.org/wiki/1960_Valdivia_earthquake)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                                           |
|:---------------------|:--------------------------------------------------------------------------------------|
| Year                 | 1960                                                                                  |
| Country              | Chile                                                                                 |
| Region               | Valdivia                                                                              |
| Event_Name           | Valdivia_1960                                                                         |
| Local_Date           | 22/05/1960                                                                            |
| Local_Time           | 15:11:14                                                                              |
| Latitude             | -38.143                                                                               |
| Longitude            | -73.407                                                                               |
| Depth_(km)           | 25                                                                                    |
| Mw                   | 9.5                                                                                   |
| Max_Intensity_(MMI)  | IX                                                                                    |
| Fault_mechanism      | Strike slip                                                                           |
| Tectonic_region_type | Subduction                                                                            |
| Fatalities           | 1000-6000                                                                             |
| Injured              | 1743-3000                                                                             |
| Displaced_Population | 2000000                                                                               |
| Affected_Population  | 2000000-2500000                                                                       |
| Affected_Units       | nan                                                                                   |
| Damaged_Units        | 58622-450000 Units                                                                    |
| Collapsed_Units      | 72 Units                                                                              |
| Economic_Losses      | 400-1000 M USD                                                                        |
| Insured_Losses       | nan                                                                                   |
| Induced_Effects      | Tsunami, Volcano, Landslides, Flood                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/official19600522191120_30/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1960_Valdivia_earthquake                                |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
