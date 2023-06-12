# 🌎 1997 M5.5 UmbriaMarche earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1997 M5.5 UmbriaMarche earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1997 Umbria and Marche earthquake occurred in the regions of Umbria and Marche, central Italy on the morning of September 26.  It was preceded by a foreshock almost as strong as the main quake.  The foreshock occurred at 02:33 CEST (00:33 UTC), rated Mw5.7, and the second – the main shock – occurred at 11:40 CEST (09:40 UTC), rated Mw 6.0. Their epicentre was in Annifo. The mainshock was assigned X (Extreme) and foreshock VIII (Severe) on the Mercalli intensity scale.There were several thousands of foreshocks and aftershocks from May 1997 to April 1998, more than thirty of which had a magnitude more than 3.5. Eleven people are known to have died following the shocks.
[Wikipedia](https://en.wikipedia.org/wiki/1997_Umbria_and_Marche_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1997                                                                   |
| Country              | Italy                                                                  |
| Region               | UmbriaMarche                                                           |
| Event_Name           | UmbriaMarche_1997                                                      |
| Local_Date           | 14/10/1997                                                             |
| Local_Time           | 15:23:10                                                               |
| Latitude             | 42.962                                                                 |
| Longitude            | 12.892                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 5.5                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0008916/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1997_Umbria_and_Marche_earthquake        |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
