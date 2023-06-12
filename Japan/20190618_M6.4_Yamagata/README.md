# 🌎 2019 M6.4 Yamagata earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2019 M6.4 Yamagata earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2019 Yamagata earthquake` struck at 22:22 JST (13:22 UTC) on 18 June 2019 with an estimated magnitude of Mw6.4 [Wikipedia](https://en.wikipedia.org/wiki/2019_Yamagata_earthquake).

According to official Japanese statistics, the earthquake caused 9 serious injuries and 34 minor injuries. Additionally, 28 houses were partially destroyed and 1,580 partially damaged.


### Type of sequence
No notes of damaging aftershocks were discovered.

### Occurrence of other phenomena: 
Tsunami (up to 10cm)

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2019                                                                   |
| Country              | Japan                                                                  |
| Region               | Yamagata                                                               |
| Event_Name           | Yamagata_2019                                                          |
| Local_Date           | 18/06/2019                                                             |
| Local_Time           | 22:22:20                                                               |
| Latitude             | 38.639                                                                 |
| Longitude            | 139.477                                                                |
| Depth_(km)           | 12                                                                     |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 0                                                                      |
| Injured              | 28-43                                                                  |
| Displaced_Population | 45-840                                                                 |
| Affected_Population  | 432                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 144-1608 Buildings                                                     |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Tsunami                                                                |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us600042fx/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2019_Yamagata_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
