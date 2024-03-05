# 🌎 1981 M6.7 GulfofCorinth earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1981 M6.7 GulfofCorinth earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

In early 1981 the eastern Gulf of Corinth, Greece was struck by three earthquakes with a magnitude greater than 6 Ms over a period of 11 days. The earthquake sequence caused widespread damage in the Corinth–Athens area, destroying nearly 8,000 houses and causing 20–22 deaths.
[Wikipedia](https://en.wikipedia.org/wiki/1981_Gulf_of_Corinth_earthquakes)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1981                                                                   |
| Country              | Greece                                                                 |
| Region               | GulfofCorinth                                                          |
| Event_Name           | GulfofCorinth_1981                                                     |
| Local_Date           | 24/02/1981                                                             |
| Local_Time           | 20:53:38                                                               |
| Latitude             | 38.222                                                                 |
| Longitude            | 22.934                                                                 |
| Depth_(km)           | 33                                                                     |
| Mw                   | 6.7                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 22                                                                     |
| Injured              | 400                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 80400                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 8000 Buildings                                                         |
| Economic_Losses      | 812-900 M USD                                                          |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0001ccb/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1981_Gulf_of_Corinth_earthquakes         |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
