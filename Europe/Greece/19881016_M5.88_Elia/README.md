# 🌎 1988 M5.9 Elia earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1988 M5.9 Elia earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The earthquake of 16 October 1988 occurred in Southwestern Greece, near the island of Zakynthos in the straits that separate the island from the Peloponnese Peninsula to the east.
[Academic Article](https://www.researchgate.net/publication/47499329_The_October_1988_Elia_Prefecture_Earthquake_SW_Greece_Seismic_Environment_Building_Types_and_Damage_Patterns)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1988                                                                   |
| Country              | Greece                                                                 |
| Region               | Elia                                                                   |
| Event_Name           | Elia_1988                                                              |
| Local_Date           | 16/10/1988                                                             |
| Local_Time           | 12:34:05                                                               |
| Latitude             | 37.938                                                                 |
| Longitude            | 20.932                                                                 |
| Depth_(km)           | 25.2                                                                   |
| Mw                   | 5.9                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | nan                                                                    |
| Injured              | nan                                                                    |
| Displaced_Population | 25                                                                     |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0003mvg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1986_Kalamata_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
