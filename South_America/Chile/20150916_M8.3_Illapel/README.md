# 🌎 2015 M8.3 Illapel earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2015 M8.3 Illapel earthquake in Chile.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `2015 Illapel earthquake` occurred 46 km (29 mi) offshore from Illapel (Coquimbo region, Chile) on September 16 at 19:54:33 Chile Standard Time (22:54:33 UTC), with a moment magnitude of 8.3-8.4. The Chilean government reported 15 deaths, 6 missing and thousands of people affected. In Buenos Aires, Argentina, a man died from a stroke while he was evacuating a building. Illapel, an inland city of 30,000 residents, was reported immediately to be without electricity or drinking water. Many towns and small cities in the Coquimbo region saw a lot of damage, where the earthquake was felt with an intensity of VIII Mercalli. The panic took over the great cities like La Serena, Valparaiso and the capital Santiago. Two days after the quake, about 90,000 people were still without electricity. On September 21, officials were reporting over 9,000 people had been left homeless by the quake. [Wikipedia](https://en.wikipedia.org/wiki/2015_Illapel_earthquake)


### Type of sequence
- This earthquake had an unusual foreshock, just 20 seconds before the main 8.3 earthquake, reaching a magnitude of 7.2. This has been considered as one of the most complex earthquakes to be ever studied in Chile. [Wikipedia](https://en.wikipedia.org/wiki/2015_Illapel_earthquake)
- The initial quake lasted between three and five minutes; it was followed by several aftershocks greater than magnitude six and two that exceeded 7.0 moment magnitude. A total of 5000 aftershocks were recorded as of June 2017, of which 31 of them were 6.0 Mw or higher. [Wikipedia](https://en.wikipedia.org/wiki/2015_Illapel_earthquake)
- The main aftershock of the Illapel earthquake occurred 24 minutes after the main earthquake and reached a magnitude of 7. During the first year after the earthquake there were 4,220 aftershocks with a magnitude greater than 3. [CSN](https://www.csn.uchile.cl/efemerides-sismicas-terremoto-de-illapel-2015/)
- The type of seismic sequence that occurred after the Illapel earthquake fits what we know of other sequences product of large contact tremors in subduction (coupling between the Nazca Plate and the South American Plate), such as the Maule earthquake in 2010 and the Iquique earthquake in 2014. [CSN](http://www.csn.uchile.cl/evaluacion-a-un-ano-del-terremoto-de-illapel/)

<img src="Chile/20150916_M8.3_Illapel/References/Aftershocks.jpg"  width="500" height="500">

Figure source: [CSN](http://www.csn.uchile.cl/evaluacion-a-un-ano-del-terremoto-de-illapel/)

- Aftershocks figures and movie for Mo 8.3 near the coast of central Chile till 2015-09-26. [IRIS](http://ds.iris.edu/spud/aftershock/10089367)
- The main shock has been followed by numerous aftershocks: Within 4 days, 57 of magnitude above 5.0, 10 of magnitude above 6.0 and one of magnitude above 7.0.

<img src="https://www.emsc-csem.org/Files/event/459672/Diapositive4.PNG"  width="550" height="400">

Figure source: [EMSC](https://www.emsc-csem.org/#2)


### Occurrence of other phenomena: 
- The first tsunami waves arrived on the Chilean coast within minutes. A series of waves reaching at least 4.5 m (15 ft) high were observed along the coast of Coquimbo and the cities of Coquimbo, Tongoy, and Concón nearby Valparaiso reported flooding; large fishing vessels were swept into the streets of Coquimbo, which reported heavy damage. The port of Coquimbo, along with the Costanera, was heavily damaged. The tsunami also damaged the iconic La Serena monumental lighthouse. In the coastal city of Tongoy, large areas along the seafront were destroyed, along with the Tongoy beach itself, which was heavily affected by both earthquake and tsunami. Across the region, at least 500 buildings were destroyed, while dozens of beachfront homes in Los Vilos were damaged or destroyed. [Wikipedia](https://en.wikipedia.org/wiki/2015_Illapel_earthquake)
- The tsunami that produced this earthquake arrived only five minutes after the earthquake occurred (according to reports from inhabitants of the coastal area near the epicentral zone), it was not expected to be so fast. [CSN](https://www.csn.uchile.cl/efemerides-sismicas-terremoto-de-illapel-2015/) 
- This earthquake generated a tsunami that was observed all over the Pacific region and caused damage locally. A 4.75 m high tsunami wave was measured on the Coquimbo, Chile sea level gauge, and 1-2 m high waves were measured elsewhere in Chile. [ITIC](http://itic.ioc-unesco.org/index.php?option=com_content&view=article&id=1946%3A16-september-2015-utc-mw-8-3-northern-chile-tsunami&catid=2164&Itemid=2616)
- The National Emergency Office (ONEMI, per its Spanish acronym) issued a tsunami warning for the entire Chilean coastal area, evacuating over 600,000 people. ONEMI reports that approximately 681,484 people were affected as a result of the earthquake, and has declared the Coquimbo region as a disaster area. A preventive evacuation status for the entire Chilean Coast was declared by the National Emergency Office (ONEMI) 11 min after the earthquake. Despite the prompt evacuation, eight causalities were attributed to the tsunami. A total of 8 (of 15) fatalities were attributed to the tsunami. In Coquimbo city, there were 6 fatalities from the tsunami. One tsunami fatalities occurred in both the cities of Tongoy and Puerto Aldea. [NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-more-info/5590)
- The main event triggered tsunami waves that damaged structures along the coast, while the surface ground motion induced localized liquefaction, settlement of bridge abutments, rockfall, debris flow, and collapse in several adobe structures. (Candia_et_al_2017)

<img src="https://ngdc.noaa.gov/hazard/img/2015_0916.jpg"  width="480" height="504">

Figure source: [NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-more-info/5590)


- Estimation of landslide by the Illapel earthquake. [CSN](http://www.csn.uchile.cl/estimacion-del-desplazamiento-que-produjo-el-terremoto-de-illapel-2015/)
- Rockfall was widespread along roads and cut slopes within the zone of deformation of the earthquake rupture leading to complete and partial blockage of travel networks. (GEERI_llapel_Earthquake_2015)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2015                                                                   |
| Country              | Chile                                                                  |
| Region               | Illapel                                                                |
| Event_Name           | Illapel_2015                                                           |
| Local_Date           | 16/09/2015                                                             |
| Local_Time           | 19:54:33                                                               |
| Latitude             | -31.5729                                                               |
| Longitude            | -71.6744                                                               |
| Depth_(km)           | 22.44                                                                  |
| Mw                   | 8.3                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 13-19                                                                  |
| Injured              | 14-34                                                                  |
| Displaced_Population | >16646                                                                 |
| Affected_Population  | 688-681499                                                             |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 1791-10685 Units                                                       |
| Collapsed_Units      | 1069-2872 Units                                                        |
| Economic_Losses      | 600-900 M USD                                                          |
| Insured_Losses       | 350 M USD                                                              |
| Induced_Effects      | Tsunami, Landslides                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us20003k7a/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2015_Illapel_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
