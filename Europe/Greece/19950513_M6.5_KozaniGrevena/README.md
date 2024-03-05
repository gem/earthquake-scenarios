# 🌎 1995 M6.6 KozaniGrevena earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1995 M6.6 KozaniGrevena earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

At 08:47 GMT, on May 13, 1995, a strong earthquake of Ms = 6.6 occurred in the NW part of Greece (Western Macedonia) and caused serious damage in the Kozani and Grevena prefectures, but fortunately no fatalities. The maximum observed macroseismic intensity was IX + of the Modified Mercalli scale. The main shock was preceded by several foreshocks and followed by intense aftershock activity lasting several months.
[Academic Paper](https://www.sciencedirect.com/science/article/abs/pii/S0264370797000689)



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
| Region               | KozaniGrevena                                                          |
| Event_Name           | KozaniGrevena_1995                                                     |
| Local_Date           | 13/05/1995                                                             |
| Local_Time           | 08:47:12                                                               |
| Latitude             | 40.149                                                                 |
| Longitude            | 21.695                                                                 |
| Depth_(km)           | 14                                                                     |
| Mw                   | 6.6                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 0-26                                                                   |
| Injured              | 25-60                                                                  |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 15000                                                                  |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 12000 Buildings                                                        |
| Economic_Losses      | 450 M USD                                                              |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0006x90/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1986_Kalamata_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
