# 🌎 1994 M6.8 Cacua earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1994 M6.8 Cacua earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- The `1994 Páez River earthquake` occurred on June 6 an Mw of 6.8 at a depth of 12 km. The event, which is also known as the Páez River disaster, included subsequent landslides and mudslides that destroyed the small town of Páez, located on the foothills of the Central Ranges of the Andes in Cauca in south-western Colombia. It was estimated that 1,100 people, mostly from the Páez, were killed in some 15 settlements in the Páez River basin, Cauca and Huila departments of which the eponymous town of Páez suffered 50% of the death toll ([Wikipedia](https://en.wikipedia.org/wiki/1994_P%C3%A1ez_River_earthquake)). 
- The municipalities that were most affected by the earthquake were Páez, Toribío, Inzá, Jambaló, and Totoró, in the department of Cauca, where vulnerable buildings collapsed, and others had severe to very severe damage ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=59)).


### Type of sequence
- There is no information about sequences.


### Occurrence of other phenomena:
- The most significant effects caused by this earthquake were those that occurred in nature: wide and deep cracks in the ground, numerous landslides, and large avalanches were remarkable phenomena in the region. Due to the superficiality of the earthquake, the winter season, and the deforestation and topography of the area, a series of large landslides were triggered that obstructed rivers and roads and destroyed homes and crops. The obstruction of the rivers generated subsequent avalanches that devastated entire populations and significantly increased the damage. For that reason, in some populations, it was difficult to differentiate the damage caused directly by the earthquake from the indirect ones, such as landslides and avalanches. Apparently, the damage caused by the earthquake was moderate to severe, while those of the landslides and avalanches were destructive ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=59)). 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1994                                                                   |
| Country              | Colombia                                                               |
| Region               | Cacua                                                                  |
| Event_Name           | Cacua_1994                                                             |
| Local_Date           | 06/06/1994                                                             |
| Local_Time           | 03:47:00                                                               |
| Latitude             | 2.89                                                                   |
| Longitude            | -75.95                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.8                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike-Slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 128-1100                                                               |
| Injured              | 158-207                                                                |
| Displaced_Population | 13000-24797                                                            |
| Affected_Population  | 12461-28569                                                            |
| Affected_Units       | 1664 Units                                                             |
| Damaged_Units        | 3160 Units                                                             |
| Collapsed_Units      | 200 Units                                                              |
| Economic_Losses      | 2.4 M USD                                                              |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, Flood, Avalanches                                          |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0006dv8/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1994_P%C3%A1ez_River_earthquake          |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
