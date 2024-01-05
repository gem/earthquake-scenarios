# 🌎 2016 M5.9 Bukoba earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2016 M5.9 Bukoba earthquake in Tanzania.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2016 Bukoba earthquake` struck at 15:27 local time on 10 September 2016 with an estimated magnitude of Mw5.9 and very strong (VII) shaking on the border between Tanzania and Uganda. Tens of people died and hundreds were injured. Hundreds to thousands of homes were destroyed. Damage estimates range widely between different sources.

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2016                                                                   |
| Country              | Tanzania, Uganda                                                       |
| Region               | Kagera                                                                 |
| Event_Name           | Bukoba_2016                                                            |
| Local_Date           | 10/09/2016                                                             |
| Local_Time           | 15:27:33                                                               |
| Latitude             | -1.0355                                                                |
| Longitude            | 31.6181                                                                |
| Depth_(km)           | 40                                                                     |
| Mw                   | 5.9                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Cratonic                                                               |
| Fatalities           | 21-23                                                                  |
| Injured              | 440                                                                    |
| Displaced_Population | 590-10000                                                              |
| Affected_Population  | 139161                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 1125-6281 Units                                                        |
| Collapsed_Units      | 118-7500 Units                                                         |
| Economic_Losses      | 458000 M USD                                                           |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10006nkx/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2016_Tanzania_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
