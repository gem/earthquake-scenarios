# 🌎 2020 M7 AegeanSea earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2020 M7 AegeanSea earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

An earthquake with a moment magnitude of 6.9–7.0 occurred on 30 October 2020 about 14 km (8.7 mi) northeast of the Greek island of Samos. Although Samos was closest to the epicentre, it was the Turkish city İzmir, 70 km (43 mi) northeast that was heavily affected—more than 700 residential and commercial structures were seriously damaged or destroyed. One hundred and seventeen people died in İzmir Province while an additional 1,034 were injured. In Greece, there were two fatalities and 19 injured. The earthquake is the deadliest in the year 2020, and the third major earthquake to strike Turkey that year. It is also the deadliest in Turkey since 2011. The event is called the Samos earthquake by the International Seismological Centre.


[Wikipedia](https://en.wikipedia.org/wiki/2020_Aegean_Sea_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2020                                                                   |
| Country              | Greece                                                                 |
| Region               | AegeanSea                                                              |
| Event_Name           | AegeanSea_2020                                                         |
| Local_Date           | 30/10/2020                                                             |
| Local_Time           | 17:51:27                                                               |
| Latitude             | 37.8973                                                                |
| Longitude            | 26.7838                                                                |
| Depth_(km)           | 21                                                                     |
| Mw                   | 7                                                                      |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 117-119                                                                |
| Injured              | 1034-1632                                                              |
| Displaced_Population | 5000-15000                                                             |
| Affected_Population  | 6034                                                                   |
| Affected_Units       | 8703 Buildings                                                         |
| Damaged_Units        | 700 Buildings                                                          |
| Collapsed_Units      | 103 Buildings                                                          |
| Economic_Losses      | 400-450 M USD                                                          |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us7000c7y0/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2020_Aegean_Sea_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
