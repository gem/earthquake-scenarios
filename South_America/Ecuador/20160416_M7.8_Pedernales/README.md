# 🌎 2016 M7.8 Pedernales earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2016 M7.8 Pedernales earthquake in Ecuador.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `2016 Ecuador earthquake` occurred at 18:58 ECT on Saturday, April 16, with an epicenter between the Pedernales and Cojimíes parishes of the Pedernales canton, in the Ecuadorian province of Manabí With an Mw=7. The earthquake was also felt strongly in the other five provinces of the Ecuadorian coast (Manabí, Esmeraldas, Guayas, Santa Elena, Los Ríos, Santo Domingo, and El Oro), several provinces of the northern highlands of the country (Carchi, Imbabura, Pichincha and the Metropolitan District of Quito), and to a lesser extent others of the central and southern highlands (Chimborazo, Cotopaxi, Tungurahua, Bolívar, Cañar, Azuay, Loja. As far as neighboring countries are concerned, the waves reached the Colombian cities of Ipiales, Pasto, Tumaco, Popayán, Cali, Pereira, Armenia, and Bogotá, while in Peru, they were felt in the departments of Tumbes, Piura, Amazonas, and Cajamarca. It was also perceived in countries as far away as Venezuela and Panama. More than a million people were affected by the earthquake. There were at least 670 deaths,4812 missing, 6274 injured in the first three days (directly affected), 28,678 sheltered, and 113 people rescued alive from the rubble ([Wikipedia](https://es.wikipedia.org/wiki/Terremoto_de_Ecuador_de_2016)). 
- The `Pedernales Earthquake` had a moment magnitude Mw 7.8 and maximum intensity of IX (EMS-98) and became the most catastrophic natural event so far this century and was felt in locations as distant as Bogotá in Colombia and Cajamarca in Peru. The earthquake was preceded by a magnitude 4.8 Mb earthquake that occurred approximately 11 minutes earlier. The Pedernales earthquake caused a large number of casualties and extensive destruction, especially on the north and central coast of Ecuador. Thus, as a direct result of the earthquake and according to official data issued by the authorities, around 700 people died, more than 7000 injured, 22000 refugees, thousands of destroyed or uninhabitable buildings, and economic losses estimated at around three billion dollars ([IGEPN](https://www.igepn.edu.ec/interactuamos-con-usted/1810-cuatro-anos-despues-del-terremoto-de-pedernales-un-testimonio-sobre-el-peligro-sismico-en-el-ecuador)).
- A detailed archive of the reports related to this event is available on [IGEPN](https://www.igepn.edu.ec/eq20160416-informes-noticias?start=0)

### Type of sequence 
- The data indicates that most of the aftershocks are superficial (<20 km in depth), as of December 31, 2017, 11 aftershocks with magnitudes greater than or equal to 6 (Mw) were recorded, these events were felt in several cities of the country ([IGEPN](https://igepn.maps.arcgis.com/apps/MapSeries/index.html?appid=5937bdf9d11347da81137ba87b3c480a)).
- The earthquake was preceded by a magnitude 4.8 Mb earthquake that occurred approximately 11 minutes earlier. Thousands of aftershocks were recorded; until December 2016, more than 2800 were located, and until December 2017, the total amounted to 3500 replicas. The aftershocks occurred mainly around the rupture zone. In 2018 and 2019, seismic activity in this region decreased considerably, without exceeding the 320 events located each year ([IGEPN](https://www.igepn.edu.ec/interactuamos-con-usted/1810-cuatro-anos-despues-del-terremoto-de-pedernales-un-testimonio-sobre-el-peligro-sismico-en-el-ecuador)).
- A detailed archive of the reports related to the aftershocks of this event is available on [IGEPN](https://www.igepn.edu.ec/eq20160416-informes-noticias?start=0) 

<img src="Ecuador/20160416_M7.8_Pedernales/References/Aftershocks.jpg"  width="500" height="500">

Figure source: [IGEPN](https://www.igepn.edu.ec/interactuamos-con-usted/1810-cuatro-anos-despues-del-terremoto-de-pedernales-un-testimonio-sobre-el-peligro-sismico-en-el-ecuador)


### Occurrence of other phenomena: 
- After the strong earthquake, the Pacific Tsunami Warning Center, located in Hawaii (United States), issued a preventive tsunami warning for Ecuador, Colombia, Costa Rica, Panama, and Peru, which was withdrawn around midnight of the same day. In addition, widespread power outages occurred in several areas of the country, leaving many people incommunicado ([Wikipedia](https://es.wikipedia.org/wiki/Terremoto_de_Ecuador_de_2016)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2016                                                                   |
| Country              | Ecuador                                                                |
| Region               | Pedernales                                                             |
| Event_Name           | Pedernales_2016                                                        |
| Local_Date           | 16/04/2016                                                             |
| Local_Time           | 06:58:34                                                               |
| Latitude             | 0.31                                                                   |
| Longitude            | -80.12                                                                 |
| Depth_(km)           | 17                                                                     |
| Mw                   | 7.8                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Shallow upper crustal                                                  |
| Fatalities           | 650-700                                                                |
| Injured              | 6274-230000                                                            |
| Displaced_Population | 28678-386985                                                           |
| Affected_Population  | 383090-1000000000                                                      |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 9180-26672 Units                                                       |
| Collapsed_Units      | 6998-36149 Units                                                       |
| Economic_Losses      | 1300-3300 M USD                                                        |
| Insured_Losses       | 560 M USD                                                              |
| Induced_Effects      | Tsunami, Landslides                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us20005j32/executive |
| Wikipedia page       | https://es.wikipedia.org/wiki/Terremoto_de_Ecuador_de_2016             |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
