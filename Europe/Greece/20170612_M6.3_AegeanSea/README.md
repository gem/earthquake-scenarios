# 🌎 2017 M6.3 AegeanSea earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M6.3 AegeanSea earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

In 21 July 2017, a large earthquake measuring 6.6 on the moment magnitude scale struck right near Bodrum, a popular town of tourism in Turkey, killing 2 and injuring hundreds. Mostly referenced as the 2017 Bodrum-Kos earthquake, this earthquake generated a tsunami which was one of the largest tsunamis in the Mediterranean Sea region.
[Wikipedia](https://en.wikipedia.org/wiki/2017_Aegean_Sea_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2017                                                                   |
| Country              | Greece                                                                 |
| Region               | AegeanSea                                                              |
| Event_Name           | AegeanSea_2017                                                         |
| Local_Date           | 12/06/2017                                                             |
| Local_Time           | 12:28:39                                                               |
| Latitude             | 38.9296                                                                |
| Longitude            | 26.365                                                                 |
| Depth_(km)           | 12                                                                     |
| Mw                   | 6.3                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 1                                                                      |
| Injured              | 11-15                                                                  |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 731                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 250 Buildings                                                          |
| Collapsed_Units      | 10 Buildings                                                           |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us20009ly0/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2017_Aegean_Sea_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
