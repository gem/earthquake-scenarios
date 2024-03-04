# 🌎 2023 M6.8 Marrakesh–Safi earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2023 M6.8 Marrakesh–Safi earthquake in Morocco.

Available information in the folders:

- Impact
- Recording stations
- Ruptures
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 8 September 2023 at 23:11 DST (22:11 UTC), an earthquake with a moment magnitude of 6.8–6.9 and maximum Mercalli intensity of VIII (Severe) struck Morocco's Marrakesh-Safi region. The earthquake's epicenter was located 73.4 km (45.6 mi) southwest of Marrakesh, near the town of Ighil in the Atlas Mountains. It occurred as a result of shallow oblique-thrust faulting beneath the mountain range. At least 2,497 deaths were reported, with most occurring outside Marrakesh. Damage was widespread, and historic landmarks in Marrakesh were destroyed. The earthquake was also felt in Spain, Portugal, Gibraltar, Mauritania, and Algeria.It is the strongest instrumentally recorded earthquake in Morocco and deadliest in the country since 1960. It is also the second deadliest earthquake of 2023 after the Turkey–Syria earthquake. The World Health Organization estimated about 300,000 people from Marrakesh and the surrounding areas were affected. Following the earthquake, many countries offered humanitarian assistance. Morocco also announced a three-day period of national mourning.
[Wikipedia](https://en.wikipedia.org/wiki/2023_Marrakesh-Safi_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="300">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="300">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2023                                                                   |
| Country              | Morocco                                                                |
| Region               | Marrakesh-Safi                                                         |
| Event_Name           | MarrakeshSafi_2023                                                     |
| Local_Date           | 08/09/2023                                                             |
| Local_Time           | 23:11:01                                                               |
| Longitude            | -8.3887                                                                |
| Latitude             | 31.0549                                                                |
| Depth_(km)           | 19                                                                     |
| Mw                   | 6.8                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us7000kufc/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2023_Marrakesh-Safi_earthquake           |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
