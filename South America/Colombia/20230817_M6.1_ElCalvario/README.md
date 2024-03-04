# 🌎 2023-08-17 M6.1 El Calvario earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2023-08-17 M6.1 El Calvario earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On August 17, 2023, at 12:04 local time, an earthquake of magnitude 6.1 and superficial depth (less than 30 kilometers) occurred in El Calvario, Meta. The event was felt mainly in the departments of Cundinamarca, Meta, Caquetá, Risaralda, Caldas, Cauca, Nariño and Santander. The Colombian Geological Service (SGC) confirmed that, since the occurrence of the main earthquake and until 2:00 p.m. on the same day, more than 20 aftershocks were registered (all located in Meta) with magnitudes ranging from 2.0 to 5.6, and with shallow depths.
[SGC](https://www2.sgc.gov.co/Noticias/tpaginas/Comunicado-sismo-17-de-agosto-de-2023.docx.pdf)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2023                                                                   |
| Country              | Colombia                                                               |
| Region               | Meta                                                                   |
| Event_Name           | El Calvario                                                            |
| Local_Date           | 2023-08-17                                                             |
| Local_Time           | 12:04:57                                                               |
| Longitude            | -73.5111                                                               |
| Latitude             | 4.4177                                                                 |
| Depth_(km)           | 15                                                                     |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow                                                         |
| Fatalities           | 0                                                                      |
| Injured              | 0                                                                      |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 252                                                                    |
| Collapsed_Units      | 20                                                                     |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us7000kp2i/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2023_central_Colombia_earthquakes        |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
