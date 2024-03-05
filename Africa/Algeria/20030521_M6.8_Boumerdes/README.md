# 🌎 2003 M6.8 Boumerdes earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2003 M6.8 Boumerdes earthquake in Algeria.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2003 Boumerdes earthquake` struck at 19:44 local time on 21 May 2003 with an estimated magnitude of Mw6.8 and violent (IX) to extreme (X) shaking. The earthquake left 2,266-2,287 dead, 10,261-11,000 injured, and 200,000 displaced. NOAA estimated 19,000 destroyed and 163,000 damaged houses. The direct economic loss was estimated to be about $5B (EM-DAT, NOAA, [Wikipedia](https://en.wikipedia.org/wiki/2003_Boumerd%C3%A8s_earthquake)).

The Boumerdès Province (Thénia, Zemmouri, Bourmerdès) experienced heavy damage. Many buildings built in the early twentieth century during the colonial rule suffered heavy damage in the Belcourt, Bab-El-Oued and El-Casbah areas in Algiers Province



### Type of sequence
The Boumerdes 2003 event at 19:44 local time is considered a main shock, which was followed by several aftershocks. Refer to Kherroubi et. al. 2017 for more information on aftershocks.


### Occurrence of other phenomena: 
A localized tsunami (3m) formed and damaged some boats.

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2003                                                                   |
| Country              | Algeria                                                                |
| Region               | Boumerdes                                                              |
| Event_Name           | Boumerdes_2003                                                         |
| Local_Date           | 21/05/2003                                                             |
| Local_Time           | 19:44:21                                                               |
| Latitude             | 36.91                                                                  |
| Longitude            | 3.71                                                                   |
| Depth_(km)           | 12                                                                     |
| Mw                   | 6.8                                                                    |
| Max_Intensity_(MMI)  | IX-X                                                                   |
| Fault_mechanism      | Dip-slip                                                               |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 2266-2287                                                              |
| Injured              | 10261-11000                                                            |
| Displaced_Population | 200000                                                                 |
| Affected_Population  | 210261                                                                 |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | 5000 M USD                                                             |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Tsunami                                                                |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000bxpg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2003_Boumerd%C3%A8s_earthquake           |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
