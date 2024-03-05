# 🌎 1995 M6.4 Dinar earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1995 M6.4 Dinar earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 1995 Dinar earthquake occurred on 1 October in Dinar (District), Afyonkarahisar, Turkey. It had an Mw magnitude of 6.2 with an epicenter close to the Dinar-Çivril fault.The earthquake occurred at a time of political instability in Turkey, with large strikes by public sector workers taking place just 11 days earlier. The disaster was preceded by a number of smaller earthquakes of up to 5.1 magnitude, the last of which had occurred on 26 September 1995. This resulted in a number of residents deciding to sleep outside their homes and possibly resulted in less deaths and injuries in the 1 October quake. When the quake occurred, 90 people were killed and more than 200 injured in the disaster.In total, 2,473 homes suffered major damage, 1,218 moderate damage and 2,076 slight damage. The Turkish government responded by constructing 5,000 new homes for those affected by the disaster.
[Wikipedia](https://en.wikipedia.org/wiki/1995_Dinar_earthquake)



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
| Country              | Turkey                                                                 |
| Region               | Dinar                                                                  |
| Event_Name           | Dinar                                                                  |
| Local_Date           | 01/10/1995                                                             |
| Local_Time           | 15:57:16                                                               |
| Latitude             | 38.063                                                                 |
| Longitude            | 30.134                                                                 |
| Depth_(km)           | 33                                                                     |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 90-95                                                                  |
| Injured              | 200-348                                                                |
| Displaced_Population | 40000                                                                  |
| Affected_Population  | 120000                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 2473-5100 Buildings                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 205.8 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000749b/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1995_Dinar_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
