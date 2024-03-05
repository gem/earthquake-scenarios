# 🌎 2012 M6.4 Ahar-Varzaghan earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2012 M6.4 Ahar-Varzaghan earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

- The `2012 East Azerbaijan earthquakes` – also known as the `Ahar earthquakes` – occurred on 11 August 2012, at 16:53 IR Time, near the cities of Ahar and Varzaqan in Iran's East Azerbaijan Province, approximately 60 km from Tabriz. They comprised a doublet separated by eleven minutes, with magnitudes of 6.4 and 6.2 Mw. At least 306 people died, and more than 3000-5000 others were injured, primarily in the rural and mountainous areas to the northeast of Tabriz (though 45 died in the city of Ahar). The shocks were felt in Armenia and the Republic of Azerbaijan, though no major damage was reported. In the area of these earthquakes, 18618 housing units were damaged, of which 5329 were completely destroyed. A total of 410 villages have been destroyed and 65 completely destroyed. To give you a balpark, the total amount of damage to East Azerbaijan provinces since the August 12 earthquake was more than 1079 billion Rials ([Wikipedia](https://en.wikipedia.org/wiki/2012_East_Azerbaijan_earthquakes)).
- Following this twin earthquakes, more than 20 villages such as Zangabad, Gourdeh, Dino, Bajebaj, Sarand, and Shahsavar have completely destroyed and cities of Varzaghan, Ahar and Heriss suffered different levels of the damage ( See [Seyed_Razzaghi_And_Ghafory_Ashtiany_2012](Iran/DRAFT_20120811_M6.5_Varzaghan/References/Razzaghi_And_Ghafory_Ashtiany_2012.pdf) in the References folder).


### Type of sequence
- At least 80 aftershocks were felt. A 5.0 quake struck three hours later and a 5.1 aftershock struck 31 km southwest of Ahar on 12 August. On 14 August, three days after the initial quakes, another 5.1 aftershocks struck the same area at a depth of 10 km. An even stronger 5.3 tremor occurred on 15 August, approximately 34 km southwest of Ahar ([Wikipedia](https://en.wikipedia.org/wiki/2012_East_Azerbaijan_earthquakes)).
- From August 12 to March 18, a total of 4322 aftershocks were recorded, of which the intensity was 3523 smaller than 2.5, 447 aftershocks between 2.5 and 3, 272 earthquakes between 3 and 4 and 45 cases between 4 and 5 ([Wikipedia](https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%DB%B1%DB%B3%DB%B9%DB%B1_%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86_%D8%B4%D8%B1%D9%82%DB%8C)).


### Occurrence of other phenomena:
- Several landslides and rock falls occurred in the stricken area, as shown in Figures 7. Most of the observed landslides and rock falls were happened next to the Khajeh- Ahar and Khajeh-Varzaghan roads. The distances of the most observed rock falls to the epicenter were less than 20 Km. No evidence of liquefaction and/or sand boiling observed in the stricken area ( See [Seyed_Razzaghi_And_Ghafory_Ashtiany_2012](Iran/DRAFT_20120811_M6.5_Varzaghan/References/Razzaghi_And_Ghafory_Ashtiany_2012.pdf) in the References folder).



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./20120811_M6.4_Ahar-Varzaghan/OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./20120811_M6.4_Ahar-Varzaghan/OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2012                                                                   |
| Country              | Iran                                                                   |
| Region               | East Azarbaijan                                                        |
| Event_Name           | Ahar-Varzaghan                                                         |
| Local_Date           | 11/08/2012                                                             |
| Local_Time           | 16:53:00                                                               |
| Longitude            | 46.86                                                                  |
| Latitude             | 38.52                                                                  |
| Depth_(km)           | 11                                                                     |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | VII                                                                    |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 253-330                                                                |
| Injured              | 1380-26000                                                             |
| Displaced_Population | 30000-36000                                                            |
| Affected_Population  | 59540-250000                                                           |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 11908-72000 Buildings                                                  |
| Collapsed_Units      | 5329-6000 Units                                                        |
| Economic_Losses      | 500-599 M USD                                                          |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Rockfall, Landslides                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000jq5p/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2012_East_Azerbaijan_earthquakes         |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
