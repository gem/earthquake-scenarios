# 🌎 2017 M7.3 Sarpole-Zahab earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M7.3 Sarpole-Zahab earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
- On 12 November 2017 at 18:18 UTC (21:48 IR and 21:18 Arabia Standard Time), the `Sarpole-Zahab earthquake` with a Mw of 7.3 occurred on the Iran–Iraq border. The hypocenter is located within the Zagros Mountains near the Iranian town of Ezgeleh, a tectonically active region that accommodates crustal shortening resulting from the collision between the Arabian Plate and the Eurasian Plate. At least eight cities including Ghasr Shirin, Ezgeleh, Salaas Babajaani, Gilan Gharb, Sar-pol Zahab, Dalahou, Eslamabad Gharb and Javaanrood and few hundred of villages were affected by this earthquake. It has at least 620-630 people killed (mainly in Iraq's Kurdish Halabja area and the Iranian Kurdish-dominated province of Kermanshah), approximately 7000-9388 injured, and about 70000 were left homeless. The highest number of deaths and injuries were reported from Qasr-e-Shirin, Sarpol-e Zahab, and Salas Babajani cities. In this earthquake, Kermanshah province, 12000-18000 urban and rural housing units were destroyed 100 percent and 15000-50000 housing units were seriously damaged. The earthquake caused high damage to infrastructure and water and sewage networks in several cities. The amount of damages was between 300 and 350 billion Tomans ([Wikipedia](https://en.wikipedia.org/wiki/2017_Iran%E2%80%93Iraq_earthquake)).The occurrence of this earthquake is the largest earthquake that rocked the Zagros area after the 1909 Silakhor Borujerd earthquake. This earthquake had a thrust focal mechanism. Parameters affecting the destruction of this event include high acceleration, wide range of frequency content, effect of the directivity, the earthquake duration and the effect of soil conditions (See [BHRC_Report_3](https://gitlab.openquake.org/risk/ecd/-/blob/Draft_Iran/Iran/DRAFT_20171112_M7.4_SarpoleZahab/References/BHRC_Report_3.pdf) in the References folder).
- In a preliminary report, the Kermanshah Governorate announced an estimated damage cost of 26 trillion IRR(ca. 84 million US$) to residential, administrative, and infrastructure facilities in the province. This was proportioned as some 8 trillion IRR (ca. 26 million US$) of damage to residential, service, and commercial units of the province, and approximately 18 trillion IRR (ca. 58 million US$) of damage to government buildings and infrastructure (See [Saffarzadeh_et_al_2019](Iran/DRAFT_20171112_M7.4_SarpoleZahab/References/Saffarzadeh_et_al_2019.pdf) in the References folder).


### Type of sequence
- The Iranian seismological centre registered at least 50 aftershocks within a few hours of the earthquake, with a total of 242 earthquakes. These aftershocks killed at least 4 and injured at least 1488 others ([Wikipedia](https://en.wikipedia.org/wiki/2017_Iran%E2%80%93Iraq_earthquake)).
- The main earthquake of November 12, 2017 was preceded by a number of foreshocks, where the largest one was a magnitude 4.5 event 43 minutes before the mainshock that warned the local residence to leave their home and possibly reduced the number of human casualties. More than 900 aftershocks have been reported (See [BHRC_Report_3](Iran/DRAFT_20171112_M7.4_SarpoleZahab/References/BHRC_Report_3.pdf) in the References folder).


### Occurrence of other phenomena: 
- According to the IIEES reconnaissance results, there have been several incidents of landslides; also, at least 200 rockfalls were reported by this team. Furthermore, few cases of liquefaction and surface rupture were observed (See [IIEES_Report_earthquake_Chapter_2](Iran/DRAFT_20171112_M7.4_SarpoleZahab/References/IIEES_Report_earthquake_Chapter_2.pdf) in the References folder).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2017                                                                   |
| Country              | Iran                                                                   |
| Region               | Kermanshah                                                             |
| Event_Name           | Sarpole-Zahab                                                          |
| Local_Date           | 12/11/2017                                                             |
| Local_Time           | 21:48:16                                                               |
| Latitude             | 34.81                                                                  |
| Longitude            | 45.91                                                                  |
| Depth_(km)           | 18.1                                                                   |
| Mw                   | 7.3                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Thrust                                                                 |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 436-660                                                                |
| Injured              | 6603-15249                                                             |
| Displaced_Population | 7000-200000                                                            |
| Affected_Population  | 200000-1645450                                                         |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 14500-90000 Units                                                      |
| Collapsed_Units      | 2000-18000 Units                                                       |
| Economic_Losses      | 84-750 M USD                                                           |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, Rockfalls, Liquefaction                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us2000bmcg/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2017_Iran%E2%80%93Iraq_earthquake        |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
