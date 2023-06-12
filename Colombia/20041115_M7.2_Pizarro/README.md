# 🌎 2004 M7.2 Pizarro earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2004 M7.2 Pizarro earthquake in Colombia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `2004 Bajo Baudo Earthquake or the Pizarro Earthquake`, was a powerful earthquake that shook the Colombian Pacific on November 15, 2004, at 04:06 UTC-5. The earthquake had a shallow depth and had its epicenter in the Pacific Ocean, 50 km southwest of the municipality of Bajo Baudo. It had a Magnitude of 7.2Mw. Damage was recorded in several buildings in Cali, the most affected was the Torres de Alicante building, which suffered damage to its walls ([Wikipedia](https://second.wiki/wiki/terremoto_de_pizarro_de_2004)).


- The partial damages that occurred in Bajo Baudó (urban and rural areas) yielded the following figures: 287 houses destroyed, 150 houses semi-destroyed, 101 houses damaged, seven schools affected, four schools fallen, four chapels damaged, three health posts damaged and two bridges fallen. Another population that presented serious damage was the city of Cali, where 45 affected constructions were reported. In Buenaventura there was a collapse of constructions, most of the stilt houses and there were also changes in sea level that affected some homes in the Pampalinda neighborhood (the low tide area). In other municipalities in the departments of Chocó, Valle del Cauca, and Cauca there was minor damage ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=68)).


### Type of sequence
- Hundreds of aftershocks were recorded, most between 1.0 and 3.5 ([Wikipedia](https://second.wiki/wiki/terremoto_de_pizarro_de_2004)).
- In the first 14 days after the occurrence of the earthquake, more than 1000 aftershocks were recorded, highlighting five with magnitudes between 4 and 4.4 (ML) and more than fifteen with magnitudes between 3.5 and 4.0 ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=68)).

<img src="Colombia/20041115_M7.2_Pizarro/References/AftershockMags_vs_time.png"  width="600" height="500">

Figure Source: [IRIS](http://ds.iris.edu/spud/aftershock/9758491)


### Occurrence of other phenomena:
- In the epicentral zone, there were phenomena of liquefaction and cracking of the soil and temporary floods associated with liquefaction ([SGS](https://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=68)). 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2004                                                                   |
| Country              | Colombia                                                               |
| Region               | Pizarro                                                                |
| Event_Name           | Pizarro_2004                                                           |
| Local_Date           | 15/11/2004                                                             |
| Local_Time           | 04:06:00                                                               |
| Latitude             | 4.69                                                                   |
| Longitude            | -77.47                                                                 |
| Depth_(km)           | 15                                                                     |
| Mw                   | 7.2                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | nan                                                                    |
| Injured              | 6-20                                                                   |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 8016                                                                   |
| Affected_Units       | 1000 Units                                                             |
| Damaged_Units        | 611-1978 Units                                                         |
| Collapsed_Units      | 154-296 Units                                                          |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Liquefaction                                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000d8gx/executive |
| Wikipedia page       | https://second.wiki/wiki/terremoto_de_pizarro_de_2004                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
