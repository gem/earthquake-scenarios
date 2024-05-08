# 🌎 2011 M6.1 Christchurch earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2011 M6.1 Christchurch earthquake in New_Zealand.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

A major earthquake occurred in Christchurch on Tuesday 22 February 2011 at 12:51 p.m. local time (23:51 UTC, 21 February). The Mw6.2 (ML6.3) earthquake struck the entire of the Canterbury region in the South Island, centred 6.7 kilometres (4.2 mi) south-east of the central business district. It caused widespread damage across Christchurch, killing 185 people, in New Zealand's fifth-deadliest disaster.
[Wikipedia](https://en.wikipedia.org/wiki/2011_Christchurch_earthquake)



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
| Country              | New_Zealand                                                            |
| Region               | Christchurch                                                           |
| Event_Name           | Christchurch_2011                                                      |
| Local_Date           | 22/02/2011                                                             |
| Local_Time           | 12:51:42                                                               |
| Longitude            | 172.68                                                                 |
| Latitude             | -43.583                                                                |
| Depth_(km)           | 5.9                                                                    |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Oblique thrust                                                         |
| Tectonic_region_type | Active shallow crustal                                                 |
| Fatalities           | 181-185                                                                |
| Injured              | 1500-7171                                                              |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 301500                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 100000                                                                 |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 15000-40000 M USD                                                      |
| Insured_Losses       | 3500-12000 M USD                                                       |
| Induced_Effects      | Liquefaction                                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000huvq/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2011_Christchurch_earthquake             |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
