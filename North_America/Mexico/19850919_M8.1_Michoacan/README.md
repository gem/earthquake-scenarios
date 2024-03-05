# 🌎 1985 M8.1 Mexico earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1985 M8.1 Mexico earthquake in Mexico.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1985 Mexico City earthquake` struck in the early morning of 19 September at 07:17:50 (CST) with a Mw of 8.0 and a MMI of IX (Violent). The event was one of the most intense ever recorded, and macroseismic waves arrived in the Valley of Mexico with unusually high energy content. The event caused severe damage to the Greater Mexico City area and the deaths of at least 5,000 people. The event caused between 3 and 4 billion USD in damage as 412 buildings collapsed and another 3,124 were seriously damaged in the city. Most of the earthquake damage was to buildings. Two reasons are the resonance in the lakebed sediments and the long duration of the shaking. The buildings most damaged were from 6 to 15 stories in height. One interesting characteristic was that many buildings had their upper floors collapse, leaving the lower floors relatively undamaged. A survey by the government of the damage done found that few buildings from one to five stories suffered serious damage; the same was true for buildings over fifteen stories. Most of the seriously damaged buildings were built between 1957 and 1976, when the city was starting to build upwards, in the six-to-fifteen floor range. In second place were buildings from before 1957, possibly because they were weakened by the earlier earthquakes. Structures built between 1976 and 1985 suffered the least damage ([Wikipedia](https://en.wikipedia.org/wiki/1985_Mexico_City_earthquake)).


### Type of sequence
- The sequence of events included a foreshock of magnitude 5.2 that occurred the prior May, the main shock on 19 September, and two large aftershocks. The first of these occurred on 20 September with a magnitude of 7.5, and the second occurred seven months later on 30 April 1986 with a magnitude of 7.0. They were located off the coast along the Middle America Trench, more than 350 kilometers (220 mi) away, but the city suffered major damage due to its large magnitude and the ancient lake bed that Mexico City sits on. At least twelve other minor aftershocks were associated with the seismic event. ([Wikipedia](https://en.wikipedia.org/wiki/1985_Mexico_City_earthquake)).

<img src="Mexico/19850919_M8.1_Michoacan/References/Aftershock.png"  width="550" height="400">

Figure source: [IRIS](http://ds.iris.edu/spud/aftershock/9753831)


### Occurrence of other phenomena: 
- A magnitude 8.1 earthquake in Michoacan, Mexico generated a tsunami that caused some damage to Lazaro Cardenas, Michoacan. A minute after the first pulse of the earthquake the sea level dropped and receded 60 meters from the coast. The short time and recession indicate a probable landslide source. There are unconfirmed reports that ships off the coast of Mexico saw waves up to 30 meters high and some fishing boats are missing ([NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-more-info/2162))
- The earthquake did produce a number of tsunamis but they were small, ranging between one and three metres (3 ft 3 in and 9 ft 10 in) in height. Ecuador reported the highest waves of 60 cm (2.0 ft) ([Wikipedia](https://en.wikipedia.org/wiki/1985_Mexico_City_earthquake)).
- The tsunami was observed in Lázaro Cárdenas and Playa Azul, in Michoacán; Ixtapa-Zihuatanejo and Acapulco, in Guerrero; and Manzanillo, Colima. The waves spread upstream along the Balsas River, and flooded the port area of Lázaro Cárdenas, Michoacán; in just 18 minutes they reached the second bridge of the city, distant 8 kilometers from the mouth of the river. In Lázaro Cárdenas, the waves reached heights of 2.5 m and in Zihuatanejo, they reached heights of up to 3 m, flooding restaurants, and hotels. The next day an aftershock with a magnitude of 7.5 was recorded, which caused another tsunami that was recorded in the tidal station of Acapulco, where the waves reached 1.20 m in height ([Gobierno de México](https://www.gob.mx/cenapred/articulos/tsunami-ocasionado-por-un-sismo-de-magnitud-8-1-en-michoacan-mexico-el-19-de-septiembre-de-1985)).
- Landslides caused damage at Atenquique, Jalisco, and near Jala, Colima. Rockslides were reported along the highways in the Ixtapa area and sand blows and ground cracks were observed at Lazaro Cardenas ([USGS](https://earthquake.usgs.gov/earthquakes/eventpage/usp0002jwe/impact)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1985                                                                   |
| Country              | Mexico                                                                 |
| Region               | Michoacán                                                              |
| Event_Name           | Mexico_Michoacan                                                       |
| Local_Date           | 19/09/1985                                                             |
| Local_Time           | 07:17:49                                                               |
| Latitude             | 18.419                                                                 |
| Longitude            | -102.468                                                               |
| Depth_(km)           | 15                                                                     |
| Mw                   | 8.1                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Intrerface                                                  |
| Fatalities           | 3192-50000                                                             |
| Injured              | 30000-150000                                                           |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 80600-2130204                                                          |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 3000-100000  Units                                                     |
| Collapsed_Units      | 757-30000 Units                                                        |
| Economic_Losses      | 3000-8000 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, Tsunami, Liquefaction                                      |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0002jwe/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1985_Mexico_City_earthquake              |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
