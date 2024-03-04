# 🌎 2016 M7 Kumamoto earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2016 M7 Kumamoto earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2016 Kumamoto earthquake` struck at 01:25 JST (16:25 UTC) on 16 April 2016 with an estimated magnitude of Mw7.0 [Wikipedia](https://en.wikipedia.org/wiki/2016_Kumamoto_earthquakes).

According to official Japanese statistics, the earthquake caused 228 deaths (including indirect deaths), 1,149 serious injuries, and 1,604 minor injuries. Additionally, 8,697 houses were completely destroyed, 34,037 partially destroyed, and 155,902 partially damaged.


### Type of sequence
The mainshock on April 16 was preceded by a Mw6.2 foreshock on April 14. Statistics regarding the impact are typically aggregated across the foreshock and the mainshock, with most of the damages caused by the mainshock. For example, Wikipedia reports 9 deaths from the foreshock and 41 deaths from the mainshock. However, the Japanese government reports a total of 228 deaths (although it notes that indirect deaths are included in the count).


### Occurrence of other phenomena: 
The Japanese government reports 200 landslides, 57 debris flows, and 123 cliff failures associated with the event. Additionally, there are some reports of minor liquefaction.

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2016                                                                   |
| Country              | Japan                                                                  |
| Region               | Kumamoto                                                               |
| Event_Name           | Kumamoto_2016                                                          |
| Local_Date           | 16/04/2016                                                             |
| Local_Time           | 01:25:06                                                               |
| Latitude             | 32.7906                                                                |
| Longitude            | 130.7543                                                               |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7                                                                      |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Active Shallow Crustal                                                 |
| Fatalities           | 50-228                                                                 |
| Injured              | 1500-2753                                                              |
| Displaced_Population | 23985-196000                                                           |
| Affected_Population  | 272763                                                                 |
| Affected_Units       | 198636 Units                                                           |
| Damaged_Units        | 189939 Units                                                           |
| Collapsed_Units      | 8697 Units                                                             |
| Economic_Losses      | 20000-22580 M USD                                                      |
| Insured_Losses       | 5000-5645 M USD                                                        |
| Induced_Effects      | Landslides, Debris flows, Cliff failures                               |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us20005iis/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2016_Kumamoto_earthquakes                |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
