# 🌎 2000 M6.5 Iceland earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2000 M6.5 Iceland earthquake in Iceland.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2000 Iceland earthquakes struck southern Iceland on June 17 and 21. There were no fatalities but three people suffered minor injuries and there was considerable damage to infrastructure. The two earthquakes were the first major seismic activity in Iceland for 88 years. The recorded magnitude of both of the main quakes was 6.5 Mwc.
[Wikipedia](https://en.wikipedia.org/wiki/2000_Iceland_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2000                                                                   |
| Country              | Iceland                                                                |
| Region               | Iceland                                                                |
| Event_Name           | Iceland                                                                |
| Local_Date           | 17/06/2000                                                             |
| Local_Time           | 15:40:41                                                               |
| Latitude             | 63.966                                                                 |
| Longitude            | -20.487                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | nan                                                                    |
| Injured              | nan                                                                    |
| Displaced_Population | 36                                                                     |
| Affected_Population  | 108                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 11.0 Buildings                                                         |
| Collapsed_Units      | 11.0 Buildings                                                         |
| Economic_Losses      | 12-20 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0009urh/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2000_Iceland_earthquakes                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
