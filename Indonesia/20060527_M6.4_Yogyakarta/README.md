# 🌎 2006 M6.4 Yogyakarta earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2006 M6.4 Yogyakarta earthquake in Indonesia.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The `2006 Yogyakarta earthquake` (also known as the Bantul earthquake) occurred at 05:54 local time on 27 May with a moment magnitude of 6.4 and a maximum MSK intensity of VIII (Damaging). Several factors led to a disproportionate amount of damage and number of casualties for the size of the shock, with more than 5,700 dead, tens of thousands injured, and financial losses of Rp 29.1 trillion ($3.1 billion). With limited effects to public infrastructure and lifelines, housing and private businesses bore the majority of damage (the 9th-century Prambanan Hindu temple compound was also affected), and the United States' National Geophysical Data Center classified the total damage from the event as extreme.
[Wikipedia](https://en.wikipedia.org/wiki/2006_Yogyakarta_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2006                                                                   |
| Country              | Indonesia                                                              |
| Region               | Yogyakarta                                                             |
| Event_Name           | Yogyakarta                                                             |
| Local_Date           | 27/05/2006                                                             |
| Local_Time           | 05:54:00                                                               |
| Longitude            | 110.446                                                                |
| Latitude             | -7.961                                                                 |
| Depth_(km)           | 12.5                                                                   |
| Mw                   | 6.4                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike slip                                                            |
| Tectonic_region_type | Shallow crustal                                                        |
| Fatalities           | 5176-5782                                                              |
| Injured              | 36299-137883                                                           |
| Displaced_Population | 600000-699295                                                          |
| Homeless             | 699295                                                                 |
| Affected_Population  | 2340745                                                                |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 127000-451000 Buildings                                                |
| Collapsed_Units      | 127000-154000 Buildings                                                |
| Economic_Losses      | 3100 M USD                                                             |
| Insured_Losses       | 40 M USD                                                               |
| Induced_Effects      | Ground movement                                                        |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000ej1c/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2006_Yogyakarta_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
