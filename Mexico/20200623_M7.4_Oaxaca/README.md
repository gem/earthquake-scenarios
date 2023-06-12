# 🌎 2020 M7.4 Oaxaca earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2020 M7.4 Oaxaca earthquake in Mexico.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- An earthquake struck the Mexican state of `Oaxaca` at 10:29 local time on June 23, 2020, with a magnitude of 7.4 Mw. The epicenter was 19 miles (31 km) from San Miguel del Puerto and 7.5 miles (12.1 km) south-southwest of Santa María Zapotitlán. The quake was felt by an estimated 49 million people in Mexico and Guatemala, with some tremors felt as far away as 640 kilometers (400 mi). Thousands of houses in Oaxaca were damaged and 10 deaths were reported. Widespread damage was reported from Oaxaca, with over 8,000 houses affected across 145 of the state's 570 municipalities. Other damaged structures included 213 schools, 15 health centers, three hospitals, 7 bridges and 25 sections of state highways. Streets and buildings were also shaken in Mexico City, and damage was observed in at least 14 buildings across the city, including the collapse of a single floor residence and 3 buildings already seriously damaged by the 2017 Puebla earthquake. Houses were scarred by wide cracks across walls and residents sought to clear debris from the streets. Experts said that its location off the coast helps explain the relatively limited damage. Most casualties were due to structural failure ([Wikipedia](https://en.wikipedia.org/wiki/2020_Oaxaca_earthquake)).
- This earthquake was felt in the state of Oaxaca, Guerrero, Chiapas, Michoacán, Jalisco, Querétaro, Morelos, Tabasco, Veracruz, Puebla, Estado de Mexico, and in Mexico City ([PAHO](https://www.paho.org/en/natural-disasters-monitoring/natural-disasters-monitoring-june-23-2020)).
- The Mexican Seismic Alerting System (SASMEX) successfully alerted for June 23, 2020, La Crucecita earthquake (Mw 7.4) in southern Mexico. The time between the alert broadcast and the initiation of strong shaking ranged from 30 s in the city of Oaxaca to 134 s in Mexico City. SASMEX warned all cities where it operates with ample time. Peak ground acceleration in key sites in Mexico City was estimated 3.5 min after the origin time of the earthquake and one minute after strong shaking began, allowing authorities to launch civil protection procedures and building inspections. Also, the earthquake of June 23, 2020 provided important lessons to further improve the performance of SASMEX (See paper Suárez_et_al_2021 in References folder).


### Type of sequence
- On 23 June 2020, As of 1:00 PM, 303 aftershocks were registered, the largest being of magnitude 4.6 ([PAHO](https://www.paho.org/en/natural-disasters-monitoring/natural-disasters-monitoring-june-23-2020)).

<img src="Mexico/20200623_M7.4_Oaxaca/References/AftershockMags_vs_time.png"  width="550" height="400">

Figure source: [IRIS](http://ds.iris.edu/spudservice/aftershock/18256938/screen?group=0&order=2&nolog=y)

- More than 300 aftershocks had been registered by June 23, with magnitudes as high as Mw4.6 (See report VERT_Phase_1 in References folder).
- Until January 31, there have been 15,776 aftershocks, the largest being of magnitude 5.7 on July 23, 2020 (See paper Velazquez_Bucio_et_al_2021 in References folder).


### Occurrence of other phenomena: 
- After the earthquake, warnings for a `tsunami` were set out for a radius of 1,600 kilometers (990 mi), allowing people to be prepared and stay alert. The highest wave that reached the coast was measured at 1.57 meters (5.2 ft) in Mazunte ([Wikipedia](https://en.wikipedia.org/wiki/2020_Oaxaca_earthquake)).
- The first peak of the tsunami of 20 cm was detected at the nearby Salina Cruz tide station 50 minutes after the earthquake, and the largest tsunami amplitude of 68 cm occurred 70 minutes later, probably due to strong local wave resonance. The first and largest peak of the tsunami waveform in the deep ocean was detected at DART 43413 located 720 km southwest of the epicenter, approximately 1 hour after the earthquake with a maximum wave amplitude of just over 0.7 cm ([NOAA](https://nctr.pmel.noaa.gov/mexico20200623/)).

<img src="https://nctr.pmel.noaa.gov/mexico20200623/images/max_amp_2020mexico.jpg"  width="500" height="400">

Figure source: [NOAA](https://nctr.pmel.noaa.gov/mexico20200623/)


- According to the State of Oaxaca government report, Three landslides on three federal roads and five on state roads (See report Environmental_Effects in References folder).



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2020                                                                   |
| Country              | Mexico                                                                 |
| Region               | Oaxaca                                                                 |
| Event_Name           | Oaxaca_2020                                                            |
| Local_Date           | 23/06/2020                                                             |
| Local_Time           | 10:29:03                                                               |
| Latitude             | 15.784                                                                 |
| Longitude            | -96.12                                                                 |
| Depth_(km)           | 22.6                                                                   |
| Mw                   | 7.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | 10                                                                     |
| Injured              | 23-25                                                                  |
| Displaced_Population | 139                                                                    |
| Affected_Population  | 24393                                                                  |
| Affected_Units       | >8000 Units                                                            |
| Damaged_Units        | 8123-10285 Units                                                       |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 75 M USD                                                               |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Tsunami, Landslides                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us6000ah9t/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2020_Oaxaca_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
