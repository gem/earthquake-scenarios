# 🌎 2011 M5.1 Lorca earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2011 M5.1 Lorca earthquake in Spain.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

{WIKI_SUMMARY}
[Wikipedia]({WIKI_URL})



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
| Country              | Spain                                                                  |
| Region               | Murcia                                                                 |
| Event_Name           | Lorca_2011                                                             |
| Local_Date           | 11/05/2011                                                             |
| Local_Time           | 18:47:25                                                               |
| Longitude            | -1.672                                                                 |
| Latitude             | 37.699                                                                 |
| Depth_(km)           | 1                                                                      |
| Mw                   | 5.1                                                                    |
| Max_Intensity_(MMI)  | VI                                                                     |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 9                                                                      |
| Injured              | 300                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 889                                                                    |
| Collapsed_Units      | 1                                                                      |
| Economic_Losses      | 700 M EUR                                                              |
| Insured_Losses       | 484.7 M EUR                                                            |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000j1en/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2011_Lorca_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
