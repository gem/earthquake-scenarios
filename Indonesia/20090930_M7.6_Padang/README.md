# 🌎 2009 M7.6 Padang  earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2009 M7.6 Padang  earthquake in Indonesia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The first of the `2009 Sumatra earthquakes` (Indonesian: Gempa bumi Sumatra 2009) occurred on 30 September off the coast of Sumatra, Indonesia with a moment magnitude of 7.6 at 17:16:10 local time. The epicenter was 45 kilometres (28 mi) west-northwest of Padang, West Sumatra, and 220 kilometres (140 mi) southwest of Pekanbaru, Riau. Government and authorities confirmed 1,115 dead, 1,214 severely injured and 1,688 slightly injured. The most deaths occurred in the areas of Padang Pariaman (675), Padang (313), Agam (80) and Pariaman (37). In addition, around 135,000 houses were severely damaged, 65,000 houses were moderately damaged and 79,000 houses were slightly damaged. An estimated 250,000 families (1,250,000 people) have been affected by the earthquake through the total or partial loss of their homes and livelihoods.
[Wikipedia](https://en.wikipedia.org/wiki/2009_Sumatra_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2009                                                                   |
| Country              | Indonesia                                                              |
| Region               | Sumatra                                                                |
| Event_Name           | Padang                                                                 |
| Local_Date           | 30/09/2009                                                             |
| Local_Time           | 17:16:00                                                               |
| Longitude            | 99.867                                                                 |
| Latitude             | -0.72                                                                  |
| Depth_(km)           | 81                                                                     |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Oblique reverse                                                        |
| Tectonic_region_type | Subduction intraslab                                                   |
| Fatalities           | 1100-1195                                                              |
| Injured              | 1214-2181                                                              |
| Displaced_Population | 451000-1250000                                                         |
| Affected_Population  | 1200000-2500000                                                        |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 144000-181665 Buildings                                                |
| Collapsed_Units      | 181665 Buildings                                                       |
| Economic_Losses      | 220022300 M USD                                                        |
| Insured_Losses       | 100 M USD                                                              |
| Induced_Effects      | Landslides, Tsunami                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000h237/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2009_Sumatra_earthquakes                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
