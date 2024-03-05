# 🌎 2021 M7.1 Guerrero earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2021 M7.1 Guerrero earthquake in Mexico.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- A moment magnitude Mw7.0 or 7.1 earthquake occurred near the city of Acapulco in the Guerrero state of Mexico at 20:47 local time on 7 September with an estimated intensity of VIII (Severe) on the MMI scale. The earthquake killed 13 people and injured at least 23 others. At least 1.6 million people in Mexico were affected by the earthquake which resulted in localized severe damage. The earthquake occurred on the anniversary of the 2017 Chiapas earthquake which measured Mw8.2. It was also the largest earthquake in Mexico since the 2020 Oaxaca earthquake. ([Wikipedia](https://en.wikipedia.org/wiki/2021_Guerrero_earthquake)).
- This earthquake affected 40 municipalities of Guerrero. The most affected municipality was Acapulco ([Suracapulco](https://suracapulco.mx/van-7-mil-920-viviendas-afectadas-por-el-sismo-son-de-acapulco-4-mil-741/)).
- Minor damage happened at Acapulco International Airport and power outages and gas leaks occurred across 20 municipalities in Guerrero. Many landslides blocked roads from Chilpancingo south to Acapulco and north to Iguala. A tsunami with a wave height of 48 cm was recorded at Acapulco ([USGS](https://earthquake.usgs.gov/earthquakes/eventpage/us7000f93v/impact))


### Type of sequence
- More than 150 aftershocks occurs in first 24 hours after earthquake. Some landslide and road blockage reports in Guerrero are expected to increase as the region experiences aftershocks following the September 7th earthquake. The largest aftershock so far is reported to be of M5.2 ([GuyCrapenter](https://www.guycarp.com/insights/2021/09/m7-0-acapulco-mexico-earthquake-rattles-guerrero-state-to-mexico-city.html)).


<img src="Mexico/20210907_M7.1_Guerrero/References/aftershocks.png"  width="550" height="400">

Figure source: [IRIS](http://ds.iris.edu/spud/momenttensor/19759038)


### Occurrence of other phenomena: 
- Approximately ten minutes after the quake struck, the Pacific Tsunami Warning Center initially issued a tsunami threat message for the earthquake which had a preliminary magnitude of Mw7.4 at 50 km depth. A small tsunami measuring 1.2 feet (0.37 m) was recorded in Acapulco at 01:54 UTC, five minutes after the mainshock. The same observation station observed a tsunami up to 48 centimeters at 02:04. The tsunami threat was called off by the Pacific Tsunami Warning Center at 03:39 UTC ([Wikipedia](https://en.wikipedia.org/wiki/2021_Guerrero_earthquake)).
- On September 10, at 13:30 local time, a landslide occurred on the Cerro del Chiquihuite hill in Tlalnepantla de Baz, Mexico City, killing two people and causing one injury. At least three people, a woman, and her two children, went missing in the immediate aftermath. The landslide brought large boulders, which destroyed four homes and buried several others near the hillside. At least 80 residents were evacuated. According to the governor of the State of Mexico, Alfredo del Mazo Maza, heavy rainfall in the city, as well as the earthquake weakened soil conditions on the hill, triggering the landslide ([Wikipedia](https://en.wikipedia.org/wiki/2021_Guerrero_earthquake)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2021                                                                   |
| Country              | Mexico                                                                 |
| Region               | Guerrero                                                               |
| Event_Name           | Guerrero_2021                                                          |
| Local_Date           | 07/09/2020                                                             |
| Local_Time           | 20:47:00                                                               |
| Latitude             | 16.82                                                                  |
| Longitude            | -99.78                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | 3-14                                                                   |
| Injured              | 20-30                                                                  |
| Displaced_Population | 15000                                                                  |
| Affected_Population  | 1600000                                                                |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 7317-12963                                                             |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 0.20-1.1 M USD                                                         |
| Insured_Losses       | 0.20 M USD                                                             |
| Induced_Effects      | Tsunami, Landslide                                                     |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us7000f93v/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2021_Guerrero_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
