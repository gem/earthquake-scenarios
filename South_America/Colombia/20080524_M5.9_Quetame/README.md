# 🌎 2008 M5.9 Quetame earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2008 M5.9 Quetame earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `2008 El Calvario earthquake` occurred in central Colombia on 24 May and measured Mw5.9. The earthquake occurred at 2:20:43 p.m. (19:20:43 UTC) at the epicenter (El Calvario, Meta). The depth was 35 km; it was superficial according to an INGEOMINAS report. The epicenter was located 35 km from Villavicencio and 50 km from Bogotá. There were 11 confirmed fatalities and 4181 injured, mostly in the towns of Puente Quetame, Fosca, Fomeque and Guayabetal in Cundinamarca, and in El Calvario, Meta. The town of Quetame, Cundinamarca was the most affected. Several houses collapsed in this small town of 6500 inhabitants. The reconstruction of the affected structures cost 10 million USD (exchange rate COP 2000). The emergency network in the Capital District was put on maximum alert. A collapse of fixed phone lines and cell phones occurred, due to the great number of people calling to find out about their relatives. The quake was also felt in cities as far away as Medellín and Bucaramanga. In Guayabetal, Meta, civil defense workers could only reach the town from Villavicencio using motorcycles, because fallen buildings blocked cars from passing. The workers found two people dead and another 26 people trapped in a bus ([Wikipedia](https://en.wikipedia.org/wiki/2008_El_Calvario_earthquake)).


- The population most affected by this earthquake was Quetame (Cundinamarca), where many commercial and residential buildings were damaged, and some collapsed. The church and several houses had to be torn down. Other affected municipalities were Fosca and Fómeque in Cundinamarca and El Calvario and San Juanito in Meta, where houses, churches, schools, and hospitals were damaged, and some of these buildings had to be demolished. In Cáqueza, there were fissures and slight cracks in some buildings in the urban area, while in the rural area, there was a strong impact on the houses, leaving some of them uninhabitable. In Guayabetal and Chipaque, minor damage was recorded. It was felt strongly in Bogotá, Villavicencio, Acacias, and Restrepo, and in some sectors of these towns, it caused breakdowns of little consideration. One of the greatest effects induced by the earthquake was the mass movements, such as flow, slippage, collapse, and detachment, which were observed especially in Quetame, Puente Quetame, Fómeque, and El Calvario. The poor construction style of the houses had an important influence on the effects of the earthquake. Constructions in adobe, without supporting structures, usually with heavy roofs and poor foundations, as well as a mixture of materials, favored the collapse of the houses ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAIntensidadesSismo&idSismo=49)). 


- The municipalities that were most affected by the earthquake were Calvario, Villavicencio, Cáqueza, Quetame, Puente Quetame, Guayabetal, Chipaque, Fosca, Fómeque, Yopal, Paz del Río and La Percepción. The people who died due to the strong movement of the tectonic plates lived in the municipalities of Quetame, Puente Quetame, and Guayabetal. The deaths were the result of landslides and collapses of large rocks that fell on the road and in some houses near these towns[Reliefweb](https://reliefweb.int/report/colombia/colombia-cerca-de-5000-personas-afectadas-por-el-sismo).


### Type of sequence
- According to the RSNC core network, 597 aftershocks with magnitudes greater than 1.5 have been recorded until June 8, with May 24 being the day of greatest occurrence with 137 events. The largest aftershock recorded from the quake had a magnitude of 4.5 (MS) and was recorded just three minutes after the main quake ([Wikipedia](https://es.wikipedia.org/wiki/Terremoto_de_El_Calvario_de_2008)).


### Occurrence of other phenomena: 
- At least 6 people were killed by a landslide in Meta. Several buildings were damaged at Quetame ([USGS](https://earthquake.usgs.gov/earthquakes/eventpage/usp000g7p6/impact)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2008                                                                   |
| Country              | Colombia                                                               |
| Region               | Quetame                                                                |
| Event_Name           | Quetame_2008                                                           |
| Local_Date           | 24/05/2008                                                             |
| Local_Time           | 14:20:00                                                               |
| Latitude             | 4.44                                                                   |
| Longitude            | -73.81                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 5.9                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Strike-Slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 5-33                                                                   |
| Injured              | 32-4181                                                                |
| Displaced_Population | 1700-9000                                                              |
| Affected_Population  | 1754-10000                                                             |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 160-2316 Units                                                         |
| Collapsed_Units      | 47-1234 Units                                                          |
| Economic_Losses      | 10 M USD                                                               |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000g7p6/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2008_El_Calvario_earthquake              |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
