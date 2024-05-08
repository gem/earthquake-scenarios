# 🌎 2017 M6.5 Puntarenas earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M6.5 Puntarenas earthquake in Costa_Rica.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance
- The `2017 Puntarenas earthquakes or Jacó earthquake` occurred 16 kilometers southeast of Jacó on Sunday, November 12, and in the City of Puntarenas on November 13, 2017, at 20:28 local time, in both places belonging to Costa Rica. It was an earthquake of magnitude 6.5 with a maximum intensity of VIII (Grave) on the Mercalli seismological scale. The earthquake killed at least 3 people. The quake was felt most severely in the provincial districts of Quepos, Parrita, and Garabito—of which Jacó is the capital. The earthquake was felt throughout Costa Rica and in some parts of Honduras and Panama. Electricity was knocked out in some areas. There was no major infrastructure damage from the tremor that hit the lightly populated area. At least one building in Jacó had been evacuated due to apparent damage, and there were reports of walls collapsing and objects falling in other parts of the country. South Jacó had lost power lines, and there were downed poles ([Wikipedia](https://en.wikipedia.org/wiki/2017_Costa_Rica_earthquake)). 


### Type of sequence
- This earthquake was followed by more than 20 aftershocks throughout the night, the first measuring 5.1 just four minutes after the first quake ([Wikipedia](https://en.wikipedia.org/wiki/2017_Costa_Rica_earthquake)).


### Occurrence of other phenomena:
- There were landslides due to this earthquake that had caused a blockage on the highway from Jacó to other cities ([Wikipedia](https://en.wikipedia.org/wiki/2017_Costa_Rica_earthquake)).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2017                                                                   |
| Country              | Costa Rica                                                             |
| Region               | Puntarenas                                                             |
| Event_Name           | Puntarenas_2017                                                        |
| Local_Date           | 12/11/2017                                                             |
| Local_Time           | 08:28:23                                                               |
| Latitude             | 9.448                                                                  |
| Longitude            | -84.544                                                                |
| Depth_(km)           | 22                                                                     |
| Mw                   | 6.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse Fault                                                          |
| Tectonic_region_type | Subduction Interface                                                   |
| Fatalities           | 2-3                                                                    |
| Injured              | nan                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us2000bmhe/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2017_Costa_Rica_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
