# 🌎 1999 M6.1 Armenia earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1999 M6.1 Armenia earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1999 Armenia, Colombia earthquake`occurred on 25 January 1999 at 13:19 with an epicenter 40 kilometers south-west of Ibagué, Colombia. The shock heavily affected the city of Armenia in the Quindío department, and about 18 other towns and 28 additional villages in the Colombian Coffee-Growers Axis region departments, and to a lesser degree, the cities of Pereira and Manizales. The earthquake had a magnitude Mw of 6.2 and was the strongest earthquake to strike Colombia in 16 years ([wikipedia_English](https://en.wikipedia.org/wiki/1999_Armenia,_Colombia_earthquake)).
- The main economic activity in the region, the Colombian coffee industry, was highly affected. About 8000 coffee farms were completely or partially destroyed, also 13.000 structures of many types of companies and industries were affected and were out of service ([wikipedia_Spanish](https://es.wikipedia.org/wiki/Terremoto_del_eje_cafetero_de_1999)).
- The most affected municipalities were Armenia, Córdoba, Pijao, Calarcá, La Tebaida, and Montenegro in Quindío, where many buildings were destroyed. Likewise, considerable damage was recorded in the municipalities of Quimbaya, Circasia, Salento, Buenavista and Filandia (Quindío), Pereira (Risaralda) and in Caicedonia, Alcalá and Ulloa (Valle). In total, there were 28 municipalities in which there was damage due to the earthquake. The city of Armenia suffered the most significant losses. In the central part of the city, between the Quindío River and the Quebrada Hojas, the neighborhoods of Brasilia Nueva, San Nicolás, Santa Fe, Rincón Santo, Uribe, Cincuentenario, Santander, Diecinueve de Enero, Gaitán and Carbones many buildings (mostly old) collapsed. There were partial collapses and severe damage in the center of the city and in the neighborhoods of Arboleda, Yolima, Guayaquil, and in part of the buildings of the University of Quindío and the Coliseo del Café. In the Florida Norte, Bavaria, and sectors surrounding Las Palmas Avenue, there was damage to masonry and, in some cases, partial fall of roofs, but the structures were not affected. Along Bolívar and Primero de Enero Avenues, in the vicinity of the San Juan de Dios Hospital, and in the El Nogal and El Laurel neighborhoods, little affectation was observed (See report sgs_earthquake19990125.pdf in Reference folder).

In a paper presented by Asfura_et_al_1999 (See Reference folder), some useful information about building damages and fatalities has been highlighted. Such as:
- Most of the damage was to one and two-story houses and apartment buildings of four or five stories. A large number of engineered buildings collapsed or had to be demolished. The Municipal Government building, a 20-story concrete frame tower with two lateral five-story separated wings suffered extensive damage and had to be evacuated. The left wing was severely damaged during the main shock and collapsed during the 17:44 aftershock.
- Very little damage was reported to water systems, although in some areas of Armenia, water was not available for three days.
- Several two-line paved roads, highways, and bridges were affected by the earthquake. Four roads were blocked and three municipalities of Quindío were isolated due to landslides.
- Hospitals and other health care centers were severely affected by the earthquake.
- The city’s fire department and all of its personnel and equipment were housed in only one facility. The building collapsed during the earthquake, destroying all the fire trucks and killing several fire fighters.
- The police department of Armenia was also centralized, and one facility housed all personnel and equipment. This building also collapsed, killing 18 policemen.


### Type of sequence
- The National Seismological Network of Colombia (RSNC), recorded a total of 138 aftershocks during the following month to the main event. The most important occurred on the same day, 1999-01-25, 4 hours after the main earthquake and had a magnitude of 5.5 (Mw).[SGC](http://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=62)
- After the main event, an intense aftershock sequence was observed as a mechanism of restoring the perturbed equilibrium in the zone. Five months after the main shock, more than 300 smaller events have been recorded by NSNC (See report Escallon_et_al_2000 in Reference folder).
- Three major aftershocks of the whole number that caused panic among the inhabitants were: A shock occurred at 15:40 (22:40 UTC) with a magnitude of 5.4 on the Richter scale. Other aftershocks were on January 29 at 23:33 (M4.2) and January 31 at 03:03 (M3.5). [wikipedia_English](https://en.wikipedia.org/wiki/1999_Armenia,_Colombia_earthquake)


### Occurrence of other phenomena: 
- The earthquake detonated a large number of landslides, most of which were of small volume, however they managed to interrupt several sectors of the tracks. These landslides were aggravated by the heavy rains that had been happening in the affected area. (See report sgs_earthquake19990125.pdf in Reference folder)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1999                                                                   |
| Country              | Colombia                                                               |
| Region               | Armenia                                                                |
| Event_Name           | Armenia_1999                                                           |
| Local_Date           | 25/01/1999                                                             |
| Local_Time           | 13:19:00                                                               |
| Latitude             | 4.432                                                                  |
| Longitude            | -75.703                                                                |
| Depth_(km)           | 15                                                                     |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike-Slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 1000-2000                                                              |
| Injured              | 4000-10000                                                             |
| Displaced_Population | 67539-250000                                                           |
| Affected_Population  | 200000-1534500                                                         |
| Affected_Units       | 45019-90474 Units                                                      |
| Damaged_Units        | 20000-61859 Units                                                      |
| Collapsed_Units      | 15000-35972 Units                                                      |
| Economic_Losses      | 1500-2630 M USD                                                        |
| Insured_Losses       | 100-150 M USD                                                          |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp00091q3/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1994_P%C3%A1ez_River_earthquake          |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
