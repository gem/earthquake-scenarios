# 🌎 2014 M6.1 Kefalonia earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2014 M6.1 Kefalonia earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 26 January 2014 at 13:55 UTC, an Mw 6.0 earthquake struck the island of Cephalonia, Greece, followed five hours later by an Mw 5.3 aftershock and by an Mw 5.9 event on 3 February 2014 at 03:08 UTC. The epicenter of theMw 6.0 event was relocated 2 km east of the town of Lixouri, and that of the Mw 5.9 event at the tip of the Gulf of Argostoli, in the northern part of the Paliki peninsula. Extensive structural damage and widespread environmental effects were induced throughout the Paliki peninsula and along the eastern coast of the Gulf of Argostoli. Quays, sidewalks, and piers were damaged in the waterfront areas of the towns of Lixouri and Argostoli, the island capital, and liquefactions, road failures, rock falls, and small landslides were observed.Most of the latter effects took place in the aftermath of the 26 January 2014 event and were reactivated one week later by the 3 February earthquake.
[Academic Paper](https://pubs.geoscienceworld.org/ssa/srl/article-abstract/86/1/124/315431/The-February-2014-Cephalonia-Earthquake-Greece-3D)



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
| Country              | Greece                                                                 |
| Region               | Kefalonia                                                              |
| Event_Name           | Kefalonia_2014                                                         |
| Local_Date           | 26/01/2014                                                             |
| Local_Time           | 13:55:42                                                               |
| Latitude             | 38.2082                                                                |
| Longitude            | 20.4528                                                                |
| Depth_(km)           | 8                                                                      |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usb000m8ch/executive |
| Wikipedia page       | no page found                                                          |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
