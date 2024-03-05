# 🌎 2018 M5.5 Osaka earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2018 M5.5 Osaka earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2018 Osaka earthquake` struck at 07:58 JST (22:58 UTC) on 18 June 2018 with an estimated magnitude of Mw5.5-5.6 [Wikipedia](https://en.wikipedia.org/wiki/2018_Osaka_earthquake).

According to official Japanese statistics, the earthquake caused 5 deaths, 10 serious injuries, and 411 minor injuries. Additionally, 3 houses were completely destroyed, 14 partially destroyed, and 8,072 partially damaged.

The earthquake triggered the national earthquake warning system, granting about 3.2 seconds of warning for Kyoto and Osaka.

### Type of sequence
The mainshock was followed by a series of weaker aftershocks.


### Occurrence of other phenomena: 
The Japanese government reports 8 fire indicidents and 1 landslide.

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2018                                                                   |
| Country              | Japan                                                                  |
| Region               | Osaka                                                                  |
| Event_Name           | Osaka_2018                                                             |
| Local_Date           | 18/06/2018                                                             |
| Local_Time           | 07:58:35                                                               |
| Latitude             | 34.825                                                                 |
| Longitude            | 135.639                                                                |
| Depth_(km)           | 10.3                                                                   |
| Mw                   | 5.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Complex (strike-slip, reverse)                                         |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 5                                                                      |
| Injured              | 417-421                                                                |
| Displaced_Population | 267-2700                                                               |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 6766-8086 Units                                                        |
| Collapsed_Units      | 3 Units                                                                |
| Economic_Losses      | 3250-7000 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslide, Fire                                                        |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us1000eu1c/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2018_Osaka_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
