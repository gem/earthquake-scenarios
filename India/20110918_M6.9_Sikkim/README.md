# 🌎 2011 M6.9 Sikkim earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2011 M6.9 Sikkim earthquake in India.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2011 Sikkim earthquake (also known as the 2011 Himalayan earthquake) occurred with a moment magnitude of 6.9 and was centered within the Kanchenjunga Conservation Area, near the border of Nepal and the Indian state of Sikkim, at 18:10 IST on Sunday, 18 September. The earthquake was felt across northeastern India, Nepal, Bhutan, Bangladesh and southern Tibet.
[Wikipedia](https://en.wikipedia.org/wiki/2011_Sikkim_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2011                                                                   |
| Country              | India, China, Nepal, Bhutan, Bangladesh                                |
| Region               | Sikkim                                                                 |
| Event_Name           | Sikkim_2011                                                            |
| Local_Date           | 18/09/2011                                                             |
| Local_Time           | 18:10:51                                                               |
| Longitude            | 88.155                                                                 |
| Latitude             | 27.73                                                                  |
| Depth_(km)           | 50                                                                     |
| Mw                   | 6.9                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Subduction intraslab                                                   |
| Fatalities           | 111-112                                                                |
| Injured              | 177-710                                                                |
| Displaced_Population | 5000-7882                                                              |
| Affected_Population  | 575200                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 34000-39000                                                            |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 22.3 M USD                                                             |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, mudslides                                                  |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000j88b/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2011_Sikkim_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
