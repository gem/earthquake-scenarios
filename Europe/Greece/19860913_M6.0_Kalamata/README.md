# 🌎 1986 M6 Kalamata earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1986 M6 Kalamata earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1986 Kalamata earthquake struck the southern Peloponnese Region of Greece on September 13 at 20:24 local time. The 12.5 km (7.8 mi) deep moment magnitude (Mw ) 5.9 earthquake had an epicenter near the coastal city of Kalamata and was assigned X (Extreme) on the Mercalli intensity scale. The earthquake was the result of normal faulting along a northwest-dipping fault and produced surface ruptures. Extensive damage was reported in Kalamata and Elaiochori. At least 20 people died and 330 were injured. Survivors sought refuge at campsites and reconstruction work lasted five years.
[Wikipedia](https://en.wikipedia.org/wiki/1986_Kalamata_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1986                                                                   |
| Country              | Greece                                                                 |
| Region               | Kalamata                                                               |
| Event_Name           | Kalamata_1986                                                          |
| Local_Date           | 13/09/1986                                                             |
| Local_Time           | 17:24:31                                                               |
| Latitude             | 37.014                                                                 |
| Longitude            | 22.176                                                                 |
| Depth_(km)           | 11.2                                                                   |
| Mw                   | 6                                                                      |
| Max_Intensity_(MMI)  | X                                                                      |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 20                                                                     |
| Injured              | 300                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 45300                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 1500 Buildings                                                         |
| Economic_Losses      | 0-745 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0002y1v/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1986_Kalamata_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
