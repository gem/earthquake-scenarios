# 🌎 2001 M7.7 Subduction earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2001 M7.7 Subduction earthquake in El_Salvador.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `January 2001 El Salvador earthquake` struck El Salvador on January 13, 2001, at 11:33:34 a.m. local time (17:33:34 UTC). The Earthquake struck with the epicenter 60 miles (100 km) SW of San Miguel, El Salvador (13.04°N 88.66°W) at a depth of 60 km. This Earthquake caused great destruction, mainly in 172 of the 262 municipalities of the country, among which can be mentioned: Santa Ana, Jayaque, Comasagua, Nueva San Salvador, San Vicente, and San Agustín. The greatest impact of the Earthquake occurred in the Colonia "Las Colinas" of Santa Tecla, where an **avalanche** of 150 thousand cubic meters of earth broke off from the Balsamo Mountain Range, burying about 200 houses and with them many people. The neighboring country of Guatemala was affected. Eight people were killed in Guatemala. The tremor was felt from Mexico City to Colombia. **Total human casualties:** 944 dead, 193 buried, 125 missing, 5565 injured, 1364160 affected, 68777 evacuations, 39000 unemployment, and 24000 artisanal fishermen affected. **Total damaged buildings:** 277953 homes, including 688 underground, 32000 micro and small enterprises destroyed, 1385 schools (109 completely destroyed), 94 hospitals, 1155 public buildings, 16 penitentiaries, 43 docks, 98 national monuments, and approximately a quarter of paved roads. **Ecconomic Loss:** According to a report by the Economic Commission for Latin America and the Caribbean (ECLAC), the total material damage was 1255.4 million dollars, of which a total of 823 million is derived only from the private sector. The earthquake of January 13 left a significant impact on the culture of the country. According to information from the National Council for Culture and Art of El Salvador (CONCULTURA), at least 28 colonial churches, of the 90 existing ones ([Wikipedia](https://en.wikipedia.org/wiki/January_2001_El_Salvador_earthquake)).  


### Type of sequence
-  As of February 2, 2001, more than 2500 aftershocks had hit El Salvador, leading to additional damage and terrorizing the inhabitants ([Wikipedia](https://en.wikipedia.org/wiki/January_2001_El_Salvador_earthquake)).


### Occurrence of other phenomena: 
- As direct effects of the earthquake, there were large landslides affecting infrastructure and human settlements. Estimation of the number of slides is difficult because individual scarps conjoin. The total has been reported as high as 16000, though it is unclear how this figure was arrived at. Damage and injuries occurred in every department of El Salvador, particularly the departments of La Libertad and Usulután. About 585 of the deaths were caused by large landslides in Santa Tecla and Comasagua. There was the loss and degradation of the soil, agricultural areas were seriously affected by the accumulation of sediments, there was damage to basins and streams due to the accumulation of debris, and there were losses in flora and fauna, which meant the loss of goods and services such as firewood, flood control, water supply, etc. There was also a decrease in fishing activity in coastal areas and considerable losses of coffee plantations. All this gave an estimated total of $67.452 billion in direct and indirect damage losses ([Wikipedia](https://en.wikipedia.org/wiki/January_2001_El_Salvador_earthquake)).

- The 2001 tsunami was observed by the people working at ports ([NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-more-info/5444)) 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2001                                                                   |
| Country              | El Salvador                                                            |
| Region               | San Miguel                                                             |
| Event_Name           | Subduction_2001                                                        |
| Local_Date           | 13/01/2001                                                             |
| Local_Time           | 11:45:00                                                               |
| Latitude             | 12.83                                                                  |
| Longitude            | -88.79                                                                 |
| Depth_(km)           | 39                                                                     |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Subduction Intraslab                                                   |
| Fatalities           | 683-1500                                                               |
| Injured              | 3440-5565                                                              |
| Displaced_Population | 45857-81486                                                            |
| Affected_Population  | 1160316-1692942                                                        |
| Affected_Units       | 222773 Units                                                           |
| Damaged_Units        | 84682-277953 Units                                                     |
| Collapsed_Units      | 38628-108261 Units                                                     |
| Economic_Losses      | 753-2000 M USD                                                         |
| Insured_Losses       | 290 M USD                                                              |
| Induced_Effects      | Landslides, Tsunami                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000a7m5/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/January_2001_El_Salvador_earthquake      |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
