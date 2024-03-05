# 🌎 2009 M6.2 Cinchona earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2009 M6.2 Cinchona earthquake in Costa_Rica.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `2009 Cinchona earthquake` occurred at 1:21:35 pm local time on January 8 with an Mwc magnitude of 6.1 and a maximum Mercalli intensity of VII (Very strong). The shock took place in northern Costa Rica, 30 kilometres (19 mi) north-northwest of San José and was felt throughout Costa Rica and in southern central Nicaragua. ([Wikipedia](https://en.wikipedia.org/wiki/2009_Cinchona_earthquake)). 


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
| Year                 | 2009                                                                   |
| Country              | Costa Rica                                                             |
| Region               | Alajuela                                                               |
| Event_Name           | Cinchona                                                               |
| Local_Date           | 08/01/2009                                                             |
| Local_Time           | 13:21:00                                                               |
| Longitude            | -84.106                                                                |
| Latitude             | 10.116                                                                 |
| Depth_(km)           | 4.6                                                                    |
| Mw                   | 6.2                                                                    |
| Max_Intensity_(MMI)  | IX in Cinchona e Isla Bonita                                           |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active shallow crustal                                                 |
| Fatalities           | 23-98                                                                  |
| Injured              | 91-100                                                                 |
| Displaced_Population | 1244-2326                                                              |
| Affected_Population  | 128527                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 518 Buildings                                                          |
| Collapsed_Units      | 518 Buildings                                                          |
| Economic_Losses      | 100-200 M USD                                                          |
| Insured_Losses       | 100 M USD                                                              |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000gscg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2009_Cinchona_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
