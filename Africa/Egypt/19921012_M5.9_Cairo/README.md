# 🌎 1992 M5.8 Cairo earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1992 M5.8 Cairo earthquake in Egypt.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `1992 Cairo earthquake` struck at 13:08 local time on 12 October 1992 with an estimated magnitude of Mw5.8 and severe (VIII) shaking. The earthquake left 545-552 dead, 6,512-9,929 injured, and 25,020-50,000 displaced. There were an estimated 9,000 severely damaged buildings and 350 destroyed buildings. The direct economic loss was estimated to be about $1.2B-4.0B (EM-DAT, NOAA, [Wikipedia](https://en.wikipedia.org/wiki/1992_Cairo_earthquake)).

Despite the moderate magnitude and depth of ~20 km, the event was still desctructive. In Cairo alone, there were 8,500 damaged buildings. Notably, a 14-storey reinforced concrete building collapsed in Heliopolis, cairo, killing 71 people. Damage statistics for Cairo have been investigated, such as by Sadek 1999. 


### Type of sequence
The Cairo 1992 event at 13:08 local time is considered a main shock, which was followed by several aftershocks. Aftershocks are summarized in Badawy and Mónus 1995.


### Occurrence of other phenomena: 
Liquqefaction was reported in areas near the epicenter.

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1992                                                                   |
| Country              | Egypt                                                                  |
| Region               | Cairo                                                                  |
| Event_Name           | Cairo_1992                                                             |
| Local_Date           | 12/10/1992                                                             |
| Local_Time           | 13:09:55                                                               |
| Latitude             | 29.778                                                                 |
| Longitude            | 31.144                                                                 |
| Depth_(km)           | 21.5                                                                   |
| Mw                   | 5.8                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Dip-slip                                                               |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 545-561                                                                |
| Injured              | 6512-12199                                                             |
| Displaced_Population | 25020-50000                                                            |
| Affected_Population  | 57700-92649                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 8300-9350 Units                                                        |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 1200-4000 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Liquefaction                                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0005f89/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1992_Cairo_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
