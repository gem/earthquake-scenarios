# 🌎 2016 M6.2 CentralItaly earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2016 M6.2 CentralItaly earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

An earthquake, measuring 6.2 ± 0.016 on the moment magnitude scale, hit Central Italy on 24 August 2016 at 03:36:32 CEST (01:36 UTC). Its epicentre was close to Accumoli, with its hypocentre at a depth of 4 ± 1 km, approximately 75 km (47 mi) southeast of Perugia and 45 km (28 mi) north of L'Aquila, in an area near the borders of the Umbria, Lazio, Abruzzo and Marche regions. As of 15 November 2016, 299 people had been killed.
[Wikipedia](https://en.wikipedia.org/wiki/August_2016_Central_Italy_earthquake)



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
| Country              | Italy                                                                  |
| Region               | CentralItaly                                                           |
| Event_Name           | CentralItaly_2016                                                      |
| Local_Date           | 24/08/2016                                                             |
| Local_Time           | 01:36:32                                                               |
| Latitude             | 42.723                                                                 |
| Longitude            | 13.1877                                                                |
| Depth_(km)           | 4.44                                                                   |
| Mw                   | 6.2                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 296-299                                                                |
| Injured              | 368-400                                                                |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 4854                                                                   |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 5000 M USD                                                             |
| Insured_Losses       | 75 M USD                                                               |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10006g7d/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/August_2016_Central_Italy_earthquake     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
