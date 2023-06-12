# 🌎 1997 M6.1 Golestan earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1997 M6.1 Golestan earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The `1997 Ardabil earthquake`occurred on 28 February with a moment magnitude of 6.1 and a maximum Mercalli intensity of VIII (Severe). The strike-slip earthquake occurred in northern Iran, near the city of Ardabil. At least 1100 people were killed, 2600 injured, 36000 homeless, 12000 houses damaged or destroyed and 160000 livestock killed in the Ardabil area of northwestern Iran. Severe damage was observed to roads, electrical power lines, communications and water distribution systems around Ardabil. Hospitals and other medical buildings were overflowing with patients as a result of the earthquake. More than 83 villages experienced some form of damage ([Wikipedia](https://en.wikipedia.org/wiki/1997_Ardabil_earthquake)).


### Type of sequence:
- Roughly 350 aftershocks followed the main Ardabil earthquake. The largest one had a magnitude of 5.2 on the Richter scale. Aid workers and rescuers approximate death toll as high as 3000 ([Wikipedia](https://en.wikipedia.org/wiki/1997_Ardabil_earthquake)). 


### Occurrence of other phenomena: 


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1997                                                                   |
| Country              | Iran                                                                   |
| Region               | Ardebil                                                                |
| Event_Name           | Golestan                                                               |
| Local_Date           | 28/02/1997                                                             |
| Local_Time           | 12:57:28                                                               |
| Longitude            | 48.06                                                                  |
| Latitude             | 38.075                                                                 |
| Depth_(km)           | 10                                                                     |
| Mw                   | 6.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike Slip                                                            |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 954-1100                                                               |
| Injured              | 2000-2600                                                              |
| Displaced_Population | 0                                                                      |
| Affected_Population  | 38600-453756                                                           |
| Affected_Units       | 0 Units                                                                |
| Damaged_Units        | 12000 Buildings                                                        |
| Collapsed_Units      | 12000-13500 Buildings                                                  |
| Economic_Losses      | 76 M USD                                                               |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0007y0b/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1997_Ardabil_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
