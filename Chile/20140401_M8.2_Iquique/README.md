# 🌎 2014 M8.2 Iquique earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2014 M8.2 Iquique earthquake in Chile.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `2014 Iquique earthquake` struck off the coast of Chile on the 1st of April, with a moment magnitude of 8.2, at 20:46 local time (23:46 UTC). The epicenter of the earthquake was approximately 95 kilometers northwest of Iquique. The megathrust earthquake triggered a tsunami of up to 2.11 meters that hit Iquique at 21:05 local time (00:05 UTC 2 April). Similar-sized tsunamis were also reported to have hit the coasts of Pisagua and Arica. Four men died of heart attacks and one woman was reported death when a wall collapsed. Electricity and water services were interrupted in the regions of Arica y Parinacota and Tarapacá. According to the Peruvian emergency services, 9 people were slightly injured, 7 households were affected, 1 temple collapsed ([Wikipedia](https://en.wikipedia.org/wiki/2014_Iquique_earthquake)).
- This earthquake affected the regions of Arica y Parinacota, Tarapacá, and Antofagasta. In terms of physical damage, the communes of Alto Hospicio and Iquique were the most affected by the earthquake (both) and the tsunami in Iquique ([Emergencia y Desastre](https://emergenciaydesastres.mineduc.cl/terremoto-iquique/)).
- There are many +20 story buildings in the affected area with similar characteristics to those affected in the February 27th, 2010 Maule’s earthquake, such as a high shear wall density and 20cm thick walls with no or poor boundary transverse reinforcement. Nonstructural damage was also much less than in the 2010s earthquake. The smaller magnitude can explain the reason for the better performance compared to the 2010 Maule’s earthquake (8.2 Mw v/s 8.8 Mw) and better soil conditions. It should be avoided to associate the 2011 seismic code changes with this better performance since no significant difference was shown between the buildings designed before or after the code was upgraded. Finally, the extended distance from the epicenter to Iquique (95 km) was a lucky factor that mitigates the earthquake´s energy before it arrived in the city ([learning_from_earthquakes](http://learningfromearthquakes.org/2014-04-01-iquique-chile/index.php?option=com_content&view=article&id=53)). 


### Type of sequence
- In the two weeks leading up to the earthquake, a sequence of foreshocks, starting with an Mw 6.7 earthquake on March 16th and including three more Mw 6.0+ events, occurring predominantly south of the April 1st mainshock epicenter and up-dip of the area of significant slip during the mainshock. (See Herman_et_al_2016 in References folder).
- This mega-earthquake follows an earthquake sequence in the region which started in January 2014 and increased since the Mw 6.7 earthquake of March 16th. From January 1st until April 3rd there were 9 M 6+, 64 M 5+, and 244 M 4+ earthquakes recorded in this region ([EMSC](https://www.emsc-csem.org/Earthquake/226/M8-1-OFFSHORE-TARAPACA-CHILE-on-April-1st-2014-at-23-46-UTC)). The earthquake sequence in the Tarapaca region since March 15th, 2014, is shown in the following figure.

<img src="https://www.emsc-csem.org/Files/event/368890/image001.png"  width="500" height="550">

Figure source: [EMSC](https://www.emsc-csem.org/Earthquake/226/M8-1-OFFSHORE-TARAPACA-CHILE-on-April-1st-2014-at-23-46-UTC)

- Aftershocks within 10 days ([IRIS](http://ds.iris.edu/spud/momenttensor/9647147)). Other aftershock maps provided in this source have been stored as `AFTER_SHOCK_2014_04_01T234645.zip`.

<img src="Chile/20140401_M8.2_Iquique/References/20140401_Map_Aftershocks.png"  width="500" height="400">

Figure source: [IRIS](http://ds.iris.edu/spud/momenttensor/9647147) 

- There were several significant aftershocks above 6.0 magnitude and many more of lower magnitude over subsequent days which shown in the following Table ([Wikipedia](https://en.wikipedia.org/wiki/2014_Iquique_earthquake)).

|   Time (Local)        |   M          |   I       |   Depth            |   Epicenter                   |
|-----------------------|--------------|-----------|--------------------|-------------------------------|
| 1 April at 20:57:58   | 6.9          |   VI      | 28.4 km (17.6 mi)  | 91 km (57 mi) WNW of Iquique  |
| 2 April at 22:58:30   | 6.5          |   VI      | 24.1 km (15.0 mi)  | 46 km (29 mi) WSW of Iquique  |  
| 2 April at 23:43:13   | 7.7          |   VII     | 22.4 km (13.0 mi)  | 53 km (33 mi) SW of Iquique   | 
| 3 April at 02:26:15   | 6.4          |   VI      | 25.0 km (16.0 mi)  | 78 km (48 mi) SW of Iquique   |


### Occurrence of other phenomena: 
This earthquake triggered a tsunami, which hit the coastal areas in northern Chile. Based on measurements of the tsunami traces, it is estimated that a tsunami 3–4 m in height hit the coast from Arica, which is near the border between Chile and Peru, to Patache, south of Iquique, a straight-line distance of approximately 260 km. The tsunami caused only minor inundations near shorelines, and caused no damage to buildings because living spaces were higher than the tsunami run-up height. Seismic damage was more extensive than that caused by the tsunami, especially in Iquique, and included the destruction of houses, buildings, and other infrastructure. It also ignited fires. In the Port of Iquique, a wharf, before earthquake-resistant improvements were implemented, was destroyed by the strong ground motions that resulted from the earthquake (see report Tomita_et_al_2016.pdf in References folder).

<img src="Chile/20140401_M8.2_Iquique/References/01apr_chile_ttvun3dm1y_04_ntwc.jpg"  width="350" height="400">

Figure source: [NOAA](https://tsunami.gov/events/PAAQ/2014/04/01/n3dm1y/1/WEAK53/ttvun3dm1y-01.jpg)

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2014                                                                   |
| Country              | Chile                                                                  |
| Region               | Iquique                                                                |
| Event_Name           | Iquique_2014                                                           |
| Local_Date           | 01/04/2014                                                             |
| Local_Time           | 20:46:50                                                               |
| Latitude             | -19.572                                                                |
| Longitude            | -70.908                                                                |
| Depth_(km)           | 38.9                                                                   |
| Mw                   | 8.2                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | 6-7                                                                    |
| Injured              | 28-200                                                                 |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 513387                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 2500-9780 Units                                                        |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 100 M USD                                                              |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Tsunami, Landslide                                                     |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usc000nzvd/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2014_Iquique_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
