# 🌎 1997 M7.2 Qayen earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1997 M7.2 Qayen earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

- The `1997 Qayen earthquake`, also known as the `Ardekul or Qayen earthquake`, struck northern Iran's Khorasan Province in the vicinity of Qaen on May 10, 1997 at 07:57 UTC (12:57 local time). The third earthquake that year to cause severe damage, it devastated the Birjand–Qayen region, killing 1567 and injuring more than 2300. The earthquake which left 50000 homeless and damaged or destroyed over 15000 homes was described as the deadliest of 1997 by the USGS. The earthquake was felt over an area of 500000 square kilometers, including in the cities of Mashhad, Kerman and Yazd. According to an Iranian radio station report, 200 villages sustained severe damage or were totally destroyed. Some 155 aftershocks caused further destruction and drove away survivors. The earthquake was later discovered to have been caused by a rupture along a fault that runs underneath the Iran–Afghanistan border. Damage was eventually estimated at $100 million (roughly 133.6 million 2008 USD). The destruction around the earthquake's epicenter was, in places, almost total; this has been attributed to poor construction practices in rural areas, and imparted momentum to a growing movement for changes in building codes for earthquake-safe buildings ([Wikipedia](https://en.wikipedia.org/wiki/1997_Qayen_earthquake)).
- Many of the more seriously damaged homes were of simple construction, with walls made of mud, adobe, or brick packed 40–50 cm thick. These materials are generally more vulnerable to the force of the earthquake, but some of the traditionally constructed homes sustained little or no damage. This was due to a range of factors, possibly including the height-to-width ratio, the lack of windows, and the quality of the materials used. In general, reinforced concrete-framed homes built after the 1979 earthquake were better able to withstand the earthquake. Those near the epicenter still sustained severe damage due to the weight of the roofs and the weak joint connections between major structural elements of the buildings ([Wikipedia](https://en.wikipedia.org/wiki/1997_Qayen_earthquake)).


### Type of sequence
- 155 aftershocks occurred and caused further destruction ([Wikipedia](https://en.wikipedia.org/wiki/1997_Qayen_earthquake)).


### Occurrence of other phenomena: 



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                                                                                               |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| Year                 | 1997                                                                                                                                      |
| Country              | Iran                                                                                                                                      |
| Region               | South Khorasan                                                                                                                            |
| Event_Name           | Qayen                                                                                                                                     |
| Local_Date           | 10/05/1997                                                                                                                                |
| Local_Time           | 12:27:00                                                                                                                                  |
| Longitude            | 59.8                                                                                                                                      |
| Latitude             | 33.82                                                                                                                                     |
| Depth_(km)           | 10                                                                                                                                        |
| Mw                   | 7.2                                                                                                                                       |
| Max_Intensity_(MMI)  | IX                                                                                                                                        |
| Fault_mechanism      | Strike Slip                                                                                                                               |
| Tectonic_region_type | Active Crustal                                                                                                                            |
| Fatalities           | 1500-1728                                                                                                                                 |
| Injured              | 2300-2600                                                                                                                                 |
| Displaced_Population | nan                                                                                                                                       |
| Affected_Population  | 72000-200166                                                                                                                              |
| Affected_Units       | nan                                                                                                                                       |
| Damaged_Units        | 5474-7000 Buildings                                                                                                                       |
| Collapsed_Units      | 10533-15000 Buildings                                                                                                                     |
| Economic_Losses      | 100-500 M USD                                                                                                                             |
| Insured_Losses       | nan                                                                                                                                       |
| Induced_Effects      | Landslides                                                                                                                                |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000820p/executive                                                                    |
| Wikipedia page       | https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87_%DB%B1%DB%B3%DB%B7%DB%B6_%D9%82%D8%A7%D8%A6%D9%86 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
