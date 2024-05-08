# 🌎 1980 M6.9 Irpinia earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1980 M6.9 Irpinia earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1980 Irpinia earthquake (Italian: Terremoto dell'Irpinia) took place in Italy on 23 November 1980, with a moment magnitude of 6.9 and a maximum Mercalli intensity of X (Extreme). It left at least 2,483 people dead, at least 7,700 injured, and 250,000 homeless.
[Wikipedia](https://en.wikipedia.org/wiki/1980_Irpinia_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1980                                                                   |
| Country              | Italy                                                                  |
| Region               | Irpinia                                                                |
| Event_Name           | Irpinia_1980                                                           |
| Local_Date           | 23/11/1980                                                             |
| Local_Time           | 18:34:53                                                               |
| Latitude             | 40.914                                                                 |
| Longitude            | 15.366                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.9                                                                    |
| Max_Intensity_(MMI)  | X                                                                      |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 4689                                                                   |
| Injured              | 7700                                                                   |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 407700                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 20000 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0001ay4/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1980_Irpinia_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
