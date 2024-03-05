# 🌎 2009-12-19 M6.0 Karonga earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2009-12-19 M6.0 Karonga earthquake in Malawi.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2009 Karonga earthquakes occurred near Karonga, Malawi in December 2009 near the northern tip of Lake Malawi in southeast Africa. The earthquakes were one of the biggest in the history of Malawi.
[Wikipedia](https://en.wikipedia.org/wiki/2009_Karonga_earthquakes)



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
| Country              | Malawi                                                                 |
| Region               | nan                                                                    |
| Event_Name           | Karonga                                                                |
| Local_Date           | 2009-12-19                                                             |
| Local_Time           | 1261264755550                                                          |
| Longitude            | 33.818                                                                 |
| Latitude             | -10.108                                                                |
| Depth_(km)           | 6                                                                      |
| Mw                   | 6.0                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | nan                                                                    |
| Tectonic_region_type | nan                                                                    |
| Fatalities           | nan                                                                    |
| Injured              | nan                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000h56x/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2009_Karonga_earthquakes                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
