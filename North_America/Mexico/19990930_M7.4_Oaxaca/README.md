# 🌎 1999 M7.4 Oaxaca earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1999 M7.4 Oaxaca earthquake in Mexico.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1999 Oaxaca earthquake` occurred on September 30 at 11:31 local time (16:31 UTC) in Oaxaca, Mexico, 60 km NNW of Puerto Ángel. The epicenter was located near San Agustin Loxicha. It had a magnitude of Mw 7.4. The maximum intensity reached MM VIII in southwestern Oaxaca and could be felt strongly in Mexico City. The torrential rains preceding and following the temblor intensified the damage of this earthquake. 35 people were reported dead. In Oaxaca state, 508 municipalities were affected by this earthquake. The archeological site of the ancient Zapotec city of Monte Alban also suffered damage in this earthquake. The earthquake left great damages that reached more than 250 million pesos throughout the State, affected more than 600 towns, thousands of homes, schools, as well as churches, being one of the most expensive earthquakes in the history of Oaxaca. ([Wikipedia](https://en.wikipedia.org/wiki/1999_Oaxaca_earthquake)).
- This earthquake only affected the State of Oaxaca. Historical buildings, dwellings, hospitals, schools and roads were mostly impacted. Some damages were also experienced in bridges and lifelines. The economic activities were not severely impaired.
- The most significant damage was observed in adobe houses that are typically made of walls without any horizontal or vertical reinforcement for continuity and confinement (See the paper presented by Singh_et_al in the Reference folder). 


### Type of sequence
- SSN reports twenty-one aftershocks in twenty days with 4.0 ≤ M ≤ 4.7 (See the paper presented by Singh_et_al in the Reference folder).

<img src="Mexico/19990930_M7.4_Oaxaca/References/AftershockMags_vs_time.png"  width="500" height="400">

Figure source: [IRIS](http://ds.iris.edu/spudservice/aftershock/9756535/screen?group=0&order=2&nolog=y)


### Occurrence of other phenomena: 
- The heavy rains which preceded and followed the earthquake compounded the loss and presented enormous difficulties in providing emergency help. Rains drenched six states of the Mexican Republic, five of which were in critical condition, provoked grave damage with a significant number of deaths, displaced, and injured (For more information, see the report Reliefweb_19991009 in the Reference folder).
- Utilities were disrupted and roads were blocked by landslides in the state of Oaxaca ([USGS](https://earthquake.usgs.gov/earthquakes/eventpage/usp0009f7v/impact)). 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1999                                                                   |
| Country              | Mexico                                                                 |
| Region               | Oaxaca                                                                 |
| Event_Name           | Oaxaca_1999                                                            |
| Local_Date           | 30/09/1999                                                             |
| Local_Time           | 11:31:13                                                               |
| Latitude             | 16.056                                                                 |
| Longitude            | -97.004                                                                |
| Depth_(km)           | 39                                                                     |
| Mw                   | 7.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 31-50                                                                  |
| Injured              | 160-215                                                                |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 115000                                                                 |
| Affected_Units       | 86628 Units                                                            |
| Damaged_Units        | 2000-45697 Units                                                       |
| Collapsed_Units      | 9538 Units                                                             |
| Economic_Losses      | 164.8 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0009f7v/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1999_Oaxaca_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
