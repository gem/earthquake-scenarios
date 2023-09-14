# 🌎 2001 M6.6 San Salvador earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2001 M6.6 San Salvador earthquake in El_Salvador.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `February 2001 El Salvador earthquake` occurred with a moment magnitude of 6.6 on 13 February at 14:22:05 UTC. The epicentre was 15 miles (30 km) E of San Salvador, El Salvador. This earthquake occurred almost exactly a month after the major earthquake in January that affected the same area of the country. It remains unclear whether or not the two events are related in any way. Some of the sectors affected by the earthquake were: Cojutepeque, San Martín, San Vicente,  San Salvador, San Miguel, San Juan Tepezontes, Santa Cruz Analquito, and Candelaria in the Department of Cuscatlán, though it was felt throughout the country and in neighboring Guatemala and Honduras. 252622-275013 people were affected by the February earthquake, of whom 315 died, a further 3399 were injured, and 37 missing. The majority of the casualties were in the departments of Cuscatlán (165 dead, 1372 injured), San Vicente (87 dead, 1220 injured), and La Paz (58-63 dead, 806 injured). A total of 44750-57008 houses were destroyed, and a further 16752 houses, 82-83 public buildings, 111 schools, 97 churches, 5 hospitals, and 36-41 other health facilities were damaged. In total, the figures combined with those of the earthquake of January 13 gave an estimated total of losses of 1603.8 million dollars, equivalent to 12.1% of GDP, 43.5% of exports, and 75% of the general budget of the nation for the year 2001 ([Wikipedia](https://en.wikipedia.org/wiki/February_2001_El_Salvador_earthquake)).  


### Type of sequence
- Just 4 days after the earthquake of February 13, a moderate one of magnitude 5.3 occurred at 14:25 local time on Saturday, February 17, whose moderate earthquake killed 2 people, and mudslides were recorded in several communities in the east of the country; there was also some damage from landslides, the epicenter of the quake was located about 76 kilometers south of San Salvador and at a focal depth of 33 kilometers.
- Meanwhile, at 12:50 pm local time on Wednesday, February 28, a magnitude 6.1 aftershock occurred, whose earthquake was felt throughout the country and outside the borders; there was 1 injured, and the epicenter of the earthquake was located about 40 kilometers south of the mouth of the Jiboa River in the Department of La Paz (El Salvador). ([Wikipedia](https://en.wikipedia.org/wiki/February_2001_El_Salvador_earthquake)).


### Occurrence of other phenomena: 
- The January earthquake triggered many landslides that were highly destructive. The February earthquake reactivated some of these landslides but also triggered new ones. So, Landslides occurred in many areas of El Salvador. Landslides were recorded in the volcanoes of Santa Ana and San Vicente, the Bálsamo mountain range, San Jacinto, and Las Pavas hills ([Wikipedia](https://en.wikipedia.org/wiki/February_2001_El_Salvador_earthquake)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2001                                                                   |
| Country              | El Salvador                                                            |
| Region               | San Salvador                                                           |
| Event_Name           | San Salvador_2001                                                      |
| Local_Date           | 13/02/2001                                                             |
| Local_Time           | 08:22:05                                                               |
| Latitude             | 13.64                                                                  |
| Longitude            | -88.94                                                                 |
| Depth_(km)           | 13                                                                     |
| Mw                   | 6.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike Slip                                                            |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 286-315                                                                |
| Injured              | 2696-3399                                                              |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 250000-279753                                                          |
| Affected_Units       | 57008 Units                                                            |
| Damaged_Units        | 14339-17084 Units                                                      |
| Collapsed_Units      | 35196-57242 Units                                                      |
| Economic_Losses      | 348.5 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000a9jv/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/February_2001_El_Salvador_earthquake     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
