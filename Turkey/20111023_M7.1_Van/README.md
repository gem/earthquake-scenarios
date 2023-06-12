# 🌎 2011 M7.1 Van earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2011 M7.1 Van earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2011 Van earthquakes occurred in eastern Turkey near the city of Van. The first earthquake happened on 23 October at 13:41 local time. The shock had a Mw magnitude of 7.1 and a maximum Mercalli intensity of VIII (Severe). It occurred at a shallow depth, causing heavy shaking across much of eastern Turkey and lighter tremors across neighboring parts of the South Caucasus and Levant. A separate earthquake within the same earthquake system happened on 9 November at 21:23 local time (19:23 UTC). The event had multiple aftershoks, over 7 of these have been greater than magnitude 5, including a M5.6 and M5.9 soon after the quake, a M6.0, 10 hours after the earthquake, and a M5.7 which caused much additional damage including collapsed houses
[Wikipedia](https://en.wikipedia.org/wiki/2011_Van_earthquakes) and
[Daniell et al 2011](https://www.researchgate.net/publication/258434207_Comparing_the_current_impact_of_the_Van_Earthquake_to_past_earthquakes_in_Eastern_Turkey?enrichId=rgreq-0eec0badb52a05532b28aa728c172c94-XXX&enrichSource=Y292ZXJQYWdlOzI1ODQzNDIwNztBUzo5NzI4MjEyMDc0OTA2OEAxNDAwMjA1MjczODc0&el=1_x_3&_esc=publicationCoverPdf)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2011                                                                   |
| Country              | Turkey                                                                 |
| Region               | Van                                                                    |
| Event_Name           | Van_2011                                                               |
| Local_Date           | 23/10/2011                                                             |
| Local_Time           | 10:41:23                                                               |
| Latitude             | 38.721                                                                 |
| Longitude            | 43.508                                                                 |
| Depth_(km)           | 18                                                                     |
| Mw                   | 7.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 604                                                                    |
| Injured              | 2608-4152                                                              |
| Displaced_Population | 22000-150000                                                           |
| Affected_Population  | 32938-700000                                                           |
| Affected_Units       | 4882-40300 Buildings                                                   |
| Damaged_Units        | 5739-33016 Buildings                                                   |
| Collapsed_Units      | 2262-2309 Buildings                                                    |
| Economic_Losses      | 1500 M USD                                                             |
| Insured_Losses       | 90 M USD                                                               |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000j9rr/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2011_Van_earthquakes                     |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
