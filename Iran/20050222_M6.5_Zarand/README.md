# 🌎 2005 M6.5 Zarand earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2005 M6.5 Zarand earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

- The 2005 Zarand earthquake affected several villages in the Kerman province of Iran on February 22 at 05:55:23 local time. The shock measured Mw = 6.4  and had an MMI of VIII. Zarand is located 740 km southeast of Tehran. The maximum recorded PGA was 0.51 g at Shirinrud dam. The United States National Earthquake Information Center and the Belgian' Centre for Research on the Epidemiology of Disasters both show that 612 died and 1411 were injured in the event. Four villages, each having around 1000 inhabitants, were reported completely destroyed, and 30% to 70% of buildings in more than 40 villages were reported damaged. It is estimated that the population of the affected area exceeds 30000. A great portion of the population of several villages is severely affected because of the poor condition of buildings. The epicenter of the quake was a mountainous and sparsely inhabited area. It is believed that the death toll could have been much higher if the quake had stricken a more densely populated area like Bam. The total economic loss was around 80 million USD. ([Wikipedia](https://en.wikipedia.org/wiki/2005_Zarand_earthquake)).
- Two villages of Dahuiyeh and Hutkan were demolished totally, where the most of the life losses were observed. The damages in the village of Hutkan were corresponded to the location of the village houses in a slop of about 45 degree. On the other hand, the damages were amplified in the epicentral region due to a heavy rain and snow fall, which caused heavier roofs, and more suitable conditions for collapse. Some of the brick houses, however, seems to survive because of their more resistant and according to their location in the flat part of the village. The macroseismic epicenter was located in a region around Dahuiyeh and the region between Dahuiyeh and Hutkan (IIEES [English](http://www.iiees.ac.ir/en/dahuiyeh-zarand-earthquake-of-22-february-2005-ms-6-5/)).



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2005                                                                   |
| Country              | Iran                                                                   |
| Region               | Kerman                                                                 |
| Event_Name           | Zarand                                                                 |
| Local_Date           | 22/02/2005                                                             |
| Local_Time           | 05:55:21                                                               |
| Longitude            | 56.746                                                                 |
| Latitude             | 30.804                                                                 |
| Depth_(km)           | 14                                                                     |
| Mw                   | 6.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Thrust                                                                 |
| Tectonic_region_type | Active Crustal                                                         |
| Fatalities           | 400-912                                                                |
| Injured              | 1000-2000                                                              |
| Displaced_Population | nan                                                                    |
| Affected_Population  | 32000-93355                                                            |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 7000-15087 Buildings                                                   |
| Collapsed_Units      | 8000-12449 Buildings                                                   |
| Economic_Losses      | 79-80 M USD                                                            |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000dgpx/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2005_Zarand_earthquake                   |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
