# 🌎 1995 M6.5 Aigio earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1995 M6.5 Aigio earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1995 Aigio earthquake struck Western Greece near the coastal city of Aigio at 03:15:48 local time on 15 June. The earthquake measured 6.4–6.5 on the moment magnitude scale (Mw ). Significant destruction occurred; building collapses left 26 dead and up to 200 injured. The earthquake had a maximum Modified Mercalli intensity of VIII (Severe), and EMS-98 intensity of IX (Destructive). The horizontal peak ground acceleration reached 0.54 g,
and ground velocity peaked at 52 cm/s (20 in/s)—the strongest ground motion ever recorded in Greece. Monetary damages reached $660 million (in 1995 USD). Only 15 minutes after the mainshock struck, a large aftershock caused more damage to Aigio. In the aftermath, several countries and organizations provided disaster aid, including search and rescue and refugee assistance operations. Faulting took place on either the Aigion fault or an unnamed offshore fault. Other faults in the region have the potential to produce earthquakes up to Mw  6.9, which poses a risk to Aigio and the rest of the Gulf of Corinth.
[Wikipedia](https://en.wikipedia.org/wiki/1995_Aigio_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1995                                                                   |
| Country              | Greece                                                                 |
| Region               | Aigio                                                                  |
| Event_Name           | Aigio_1995                                                             |
| Local_Date           | 15/06/1995                                                             |
| Local_Time           | 00:15:48                                                               |
| Latitude             | 38.401                                                                 |
| Longitude            | 22.283                                                                 |
| Depth_(km)           | 14.2                                                                   |
| Mw                   | 6.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 26                                                                     |
| Injured              | 60-200                                                                 |
| Displaced_Population | 2100-6300                                                              |
| Affected_Population  | 13900                                                                  |
| Affected_Units       | 3400 Buildings                                                         |
| Damaged_Units        | 2300 Buildings                                                         |
| Collapsed_Units      | 2000 Buildings                                                         |
| Economic_Losses      | 422.7-660 M USD                                                        |
| Insured_Losses       | 0.2 M USD                                                              |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0006z34/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1995_Aigio_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
