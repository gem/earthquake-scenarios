# 🌎 2010 M7.0 Canterbury earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2010 M7.0 Canterbury earthquake in New_Zealand.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2010 Canterbury earthquake (also known as the Darfield earthquake) struck the South Island of New Zealand with a moment magnitude of 7.1 at 4:35 am local time on 4 September, and had a maximum perceived intensity of X (Extreme) on the Mercalli intensity scale. Some damaging aftershocks followed the main event, the strongest of which was a magnitude 6.3 shock known as the Christchurch earthquake that occurred nearly six months later on 22 February 2011. Because this aftershock was centred very close to Christchurch, it was much more destructive and resulted in the deaths of 185 people.The earthquake on 4 September caused widespread damage and several power outages, particularly in the city of Christchurch, New Zealand's second largest city at that time. Two residents were seriously injured, one by a collapsing chimney and a second by flying glass. One person died of a heart attack suffered during the quake. Another person died after a fall during the quake. Mass fatalities were avoided partly due to there being few houses of unreinforced construction, although this was also aided by the quake occurring during the early hours of the morning when most people were off the street.The earthquake's epicentre was 40 kilometres (25 mi) west of Christchurch, close to the town of Darfield. The hypocentre was at a depth of 10 km. A foreshock of roughly magnitude 5.8 hit five seconds before the main quake, and strong aftershocks were reported, up to magnitude 5.4.
[Wikipedia](https://en.wikipedia.org/wiki/2010_Canterbury_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2010                                                                   |
| Country              | New_Zealand                                                            |
| Region               | Canterbury                                                             |
| Event_Name           | Canterbury_2010                                                        |
| Local_Date           | 04/09/2010                                                             |
| Local_Time           | 04:35:47                                                               |
| Longitude            | 171.83                                                                 |
| Latitude             | -43.522                                                                |
| Depth_(km)           | 12                                                                     |
| Mw                   | 7.0                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active shallow crustal                                                 |
| Fatalities           | 0                                                                      |
| Injured              | 2-2256                                                                 |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 6500 M USD                                                             |
| Insured_Losses       | 2000-5000 M USD                                                        |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000hk46/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2010_Canterbury_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
