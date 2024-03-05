# 🌎 1999 M7.2 Duzce earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1999 M7.2 Duzce earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1999 Düzce earthquake occurred on 12 November at 18:57:22 local time with a moment magnitude of 7.2 and a maximum Mercalli intensity of IX (Violent), causing damage and at least 845 fatalities in Düzce, Turkey. The epicenter was approximately 100 km (62 mi) to the east of the extremely destructive 1999 İzmit earthquake that happened nearly three months earlier. Both strike-slip earthquakes were caused by movement on the North Anatolian Fault.
[Wikipedia](https://en.wikipedia.org/wiki/1999_D%C3%BCzce_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1999                                                                   |
| Country              | Turkey                                                                 |
| Region               | Duzce                                                                  |
| Event_Name           | Duzce_1999                                                             |
| Local_Date           | 12/11/1999                                                             |
| Local_Time           | 16:57:19                                                               |
| Latitude             | 40.758                                                                 |
| Longitude            | 31.161                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7.2                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 845-894                                                                |
| Injured              | 4948                                                                   |
| Displaced_Population | 55000                                                                  |
| Affected_Population  | 224948                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 1000 M USD                                                             |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0009hev/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1999_D%C3%BCzce_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
