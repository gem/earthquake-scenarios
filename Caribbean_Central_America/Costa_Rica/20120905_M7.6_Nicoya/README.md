# 🌎 2012 M7.6 Nicoya earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2012 M7.6 Nicoya earthquake in Costa_Rica.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `2012 Costa Rica earthquake` occurred at 08:42 local time (14:42 UTC) on September 5. The epicenter of the 7.6 Mw earthquake was in the `Nicoya` Peninsula, 11 kilometers east-southeast of Nicoya. A tsunami warning was issued shortly afterwards, but later cancelled. Two people are known to have died, one from a heart attack and another, a construction worker, crushed by a collapsing wall. It was the second strongest earthquake recorded in Costa Rica's history, following the 1991 Limon earthquake. ([Wikipedia](https://en.wikipedia.org/wiki/2012_Costa_Rica_earthquake)). 


### Type of sequence


### Occurrence of other phenomena:



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2012                                                                   |
| Country              | Costa Rica                                                             |
| Region               | Guanacaste                                                             |
| Event_Name           | Nicoya                                                                 |
| Local_Date           | 05/09/2012                                                             |
| Local_Time           | 08:42:00                                                               |
| Longitude            | -85.545                                                                |
| Latitude             | 9.828                                                                  |
| Depth_(km)           | 15.4                                                                   |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Purely inverse                                                         |
| Tectonic_region_type | Subduction interface                                                   |
| Fatalities           | 1-2                                                                    |
| Injured              | 20-225                                                                 |
| Displaced_Population | 1474                                                                   |
| Affected_Population  | 537                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 45 M USD                                                               |
| Insured_Losses       | 32 M USD                                                               |
| Induced_Effects      | Tsunami, landslides                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000jrsw/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2012_Costa_Rica_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
