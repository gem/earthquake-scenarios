# 🌎 2018 M6.6 HokkaidoEasternIburi earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2018 M6.6 HokkaidoEasternIburi earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2018 Hokkaido Eastern Iburi earthquake` struck at 03:08 JST (18:07 UTC) on 5 September 2018 with an estimated magnitude of Mw6.6 [Wikipedia](https://en.wikipedia.org/wiki/2018_Hokkaido_Eastern_Iburi_earthquake).

According to official Japanese statistics, the earthquake caused 42 deaths, 31 serious injuries, and 731 minor injuries. Additionally, 462 houses were completely destroyed, 1,570 partially destroyed, and 12,600 partially damaged. A total of 2,456 non-residential buildings were also reported as damaged.


### Type of sequence
Many months later (21 February 2019) a M_JMA 5.7 aftershock was recorded, but did not incur major damage. 

### Occurrence of other phenomena: 
Multiple landslides and debris flow instances were reported. A fire also occurred at a petroleum complex faciliy and a thermal power plant facility.

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
| Region               | Hokkaido                                                               |
| Event_Name           | HokkaidoEasternIburi_2018                                              |
| Local_Date           | 06/09/2018                                                             |
| Local_Time           | 03:08:58                                                               |
| Latitude             | 42.686                                                                 |
| Longitude            | 141.929                                                                |
| Depth_(km)           | 35                                                                     |
| Mw                   | 6.6                                                                    |
| Max_Intensity_(MMI)  | X                                                                      |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 41-44                                                                  |
| Injured              | 660-762                                                                |
| Displaced_Population | 1989-12000                                                             |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 14170-15000 Units                                                      |
| Collapsed_Units      | 462 Units                                                              |
| Economic_Losses      | 1250-2000 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, Debris flows, fires                                        |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us2000h8ty/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2018_Hokkaido_Eastern_Iburi_earthquake   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
