# 🌎 1995 M6.9 Kobe earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1995 M6.9 Kobe earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

An earthquake occurred on January 17, 1995, at 05:46:53 JST (January 16 at 20:46:53 UTC) in the southern part of Hyōgo Prefecture, Japan, including the region known as Hanshin. It measured 6.9 on the moment magnitude scale and had a maximum intensity of 7 on the JMA Seismic Intensity Scale (XI–XII on the Modified Mercalli Intensity Scale). The tremors lasted for approximately 20 seconds. The focus of the earthquake was located 17 km beneath its epicenter, on the northern end of Awaji Island, 20 km away from the center of the city of Kobe.
[Wikipedia](https://en.wikipedia.org/wiki/Great_Hanshin_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1995                                                                   |
| Country              | Japan                                                                  |
| Region               | Kobe                                                                   |
| Event_Name           | Kobe_1995                                                              |
| Local_Date           | 17/01/1995                                                             |
| Local_Time           | 05:46:52                                                               |
| Longitude            | 135.018                                                                |
| Latitude             | 34.583                                                                 |
| Depth_(km)           | 21.9                                                                   |
| Mw                   | 6.9                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Right-lateral strike slip                                              |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 5297-6434                                                              |
| Injured              | 34492-43792                                                            |
| Displaced_Population | 251301–310000                                                          |
| Affected_Population  | 541636                                                                 |
| Affected_Units       | >200000                                                                |
| Damaged_Units        | 274182-400000                                                          |
| Collapsed_Units      | 100000-186175                                                          |
| Economic_Losses      | 100000-200000 M USD                                                    |
| Insured_Losses       | 3000 M USD                                                             |
| Induced_Effects      | Fires                                                                  |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0006rew/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/Great_Hanshin_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
