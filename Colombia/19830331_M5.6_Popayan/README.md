# 🌎 1983 M5.6 Popayán earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1983 M5.6 Popayán earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1983 Popayán earthquake` occurred on 31 March in Popayán, Colombia. It had a magnitude of at least 5.5, with an epicenter southwest of Popayán at a depth of 12–15 kilometers. Although it lasted less than half a minute, damage to property was extensive, and 267 people were killed (For more information about the distribution of deaths by cause and sex, refer to Gueri_et_al_1984 in the Reference folder), with a further 7,500 people injured. In total, 14,000 buildings were damaged, the majority of them in the city's historic center. 6,885 of them suffered damage greater than 50% to the structure and a further 4,500 minor damage. 2,470 houses collapsed. Approximately $500 million (The corrected value is based on Lomnitz_et_al_1985 as the Wikipedia reference) of damage was caused. Serious damage was also caused to local infrastructure. The residents were left without electricity and water, communications were affected, and the town's airport was damaged. The quake also affected many of the neighboring towns and regions, and in Cajibio, at least ten people were killed. This earthquake resulted in the passing of new laws requiring earthquake-resistant building materials in zones at risk of tremors ([Wikipedia](https://en.wikipedia.org/wiki/1983_Popay%C3%A1n_earthquake)).


- This earthquake occurred on the Thursday of Holy Week 1983 and affected the department of Cauca, mainly the towns of Cajete, Cajibío, Julumito, Popayán and Timbío. The greatest attention was paid to the city of Popayán since approximately 200 people died there and because much of the architectural and historical heritage located in the center of the city presented severe damage and collapsed. The number of victims was high because the earthquake occurred on Easter. Public health problems began to be seen in a few days. Stomach and respiratory conditions were the main health problems. Other towns that were greatly affected were Cajete and Cajibío, which were 80 percent destroyed. In Julumito and Timbío, numerous buildings collapsed, including schools and churches ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=60#)).


- The buildings affected were in the range of 3 to 5 stories (For more information about the behavior of buildings during this earthquake, refer to Garcia_1984 in the Reference folder.).


### Type of sequence
- Heartfelt aftershocks were reported until the end of April of that year ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=60#)).


### Occurrence of other phenomena: 
- Landslides and cracks were generated in the ground in the towns of Cajete, Popayán, Julumito, Figueroa, Rio Hondo and Santa Ana ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=60#)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1983                                                                   |
| Country              | Colombia                                                               |
| Region               | Popayán                                                                |
| Event_Name           | Popayán_1983                                                           |
| Local_Date           | 31/03/1983                                                             |
| Local_Time           | 08:12:00                                                               |
| Latitude             | 2.364                                                                  |
| Longitude            | -76.696                                                                |
| Depth_(km)           | 15                                                                     |
| Mw                   | 5.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-Slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 200-350                                                                |
| Injured              | 1200-7500                                                              |
| Displaced_Population | 10000-30000                                                            |
| Affected_Population  | 10000-36200                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 13650-14000 Units                                                      |
| Collapsed_Units      | 2470-4964 Units                                                        |
| Economic_Losses      | 38-50 M USD                                                            |
| Insured_Losses       | 4 M USD                                                                |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0001u34/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1983_Popay%C3%A1n_earthquake             |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
