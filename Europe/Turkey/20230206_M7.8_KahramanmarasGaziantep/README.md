# 🌎 2023 M7.8 CentralTurkey earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2023 M7.8 CentralTurkey earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 6 February 2023, at 04:17 TRT (01:17 UTC), a Mw 7.8 earthquake struck southern and central Turkey and northern and western Syria. The epicenter was 37 km (23 mi) west–northwest of Gaziantep. The earthquake had a maximum Mercalli intensity of XII (Extreme) in parts of Antakya in Hatay Province. It was followed by a Mw 7.7 earthquake at 13:24. This earthquake was centered 95 km (59 mi) north-northeast from the first. There was widespread damage and tens of thousands of fatalities.
The Mw 7.8 earthquake is the largest in Turkey since the 1939 Erzincan earthquake of the same magnitude, and jointly the second-strongest recorded in the history of the country, after the 1668 North Anatolia earthquake. It is also one of the strongest earthquakes ever recorded in the Levant. It was felt as far as Egypt, Israel, Palestine, Lebanon, Cyprus,  and the Black Sea coast of Turkey. There were more than 10,000 aftershocks in the three weeks that followed. The seismic sequence was the result of shallow strike-slip faulting.
There was widespread damage in an area of about 350,000 km2 (140,000 sq mi) (about the size of Germany). An estimated 14 million people, or 16 percent of Turkey's population, were affected. Development experts from the United Nations estimated that about 1.5 million people were left homeless.As of 10 March 2023, more than 55,700 deaths were confirmed: more than 48,400 in Turkey, and more than 7,200 in Syria. It is the deadliest earthquake in what is present day Turkey since the 526 Antioch earthquake, making it the deadliest natural disaster in its modern history. It is also the deadliest in what is present day Syria since the 1822 Aleppo earthquake; the deadliest worldwide since the 2010 Haiti earthquake; and the fifth-deadliest of the 21st century. Damages were estimated at over US$100 billion in Turkey and US$5.1 billion in Syria, making them the fourth-costliest earthquakes on record.
Damaged roads, winter storms, and disruption to communications hampered the Disaster and Emergency Management Presidency's rescue and relief effort, which included a 60,000-strong search-and-rescue force, 5,000 health workers and 30,000 volunteers. Following Turkey's call for international help, more than 141,000 people from 94 countries joined the rescue effort.


[Wikipedia](https://en.wikipedia.org/wiki/2023_Turkey%E2%80%93Syria_earthquake)



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
| Country              | Turkey                                                                 |
| Region               | CentralTurkey                                                          |
| Event_Name           | CentralTurkey_2023                                                     |
| Local_Date           | 06/02/2023                                                             |
| Local_Time           | 01:17:34                                                               |
| Latitude             | 37.2199                                                                |
| Longitude            | 37.0189                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7.8                                                                    |
| Max_Intensity_(MMI)  | XII                                                                    |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 53227-55690                                                            |
| Injured              | 114770-129500                                                          |
| Displaced_Population | 1500000                                                                |
| Affected_Population  | nan                                                                    |
| Affected_Units       | 140000 Units                                                           |
| Damaged_Units        | 42500 Units                                                            |
| Collapsed_Units      | 15910 Units                                                            |
| Economic_Losses      | 103000 M USD                                                           |
| Insured_Losses       | 1000 M USD                                                             |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us6000jllz/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2023_Turkey%E2%80%93Syria_earthquake     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
