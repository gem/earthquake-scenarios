# 🌎 2003 M6.6 Bam earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2003 M6.6 Bam earthquake in Iran.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

- The `2003 Bam earthquake` struck the Kerman province of southeastern Iran at 01:56 UTC (5:26 am IR Time) on December 26. The shock had a moment magnitude of 6.6 and a MMI of IX (Violent). Important causes of High Casualties were: Earthquake strength, Shallow earthquake depth, The proximity of the earthquake epicenter to the city, Long duration of the earthquake, Time of the earthquake, The earthquake happened on Friday (during the Iranian weekend), High acceleration of the earthquake (vertical acceleration was equal to g), In addition to the above-mentioned reasons, most of the buildings in Bam city were not strong enough. The earthquake was particularly destructive in Bam, with the death toll amounting to at least 26271-50000 people and injuring up to 22628-200000. The effects of the earthquake were exacerbated by the use of mud brick as the standard construction medium; many of the area's structures did not comply with earthquake regulations set in 1989. 11000 students were killed and 1/5 of the 5400 local teaching staff were also. This caused a significant problem for the local education system. Up to 90% of buildings and infrastructures in the Bam area were either damaged or destroyed, with 70% of houses being completely destroyed, plus 70–90% of Bam's residential areas. This event left an estimated 45000-100000 homeless. Not a single house was standing in Baravat (Wikipedia [English](https://en.wikipedia.org/wiki/2003_Bam_earthquake) and [Persian](https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87_%DB%B1%DB%B3%DB%B8%DB%B2_%D8%A8%D9%85)). 


### Type of sequence:
- The first foreshocks of this great earthquake began in June 2003. Then, in August, two relatively severe earthquakes with magnitudes of 5 Richter occurred in the region. Also, from a long time ago, there was an unpleasant smell and sounds from wells in the region, the water of wells and aqueducts had gotten warmer, some wells were more watery and some were less watery, and all of this was signs of unusual activities on earth ([Wikipedia](https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87_%DB%B1%DB%B3%DB%B8%DB%B2_%D8%A8%D9%85)).
- Three moderate earthquakes occurred before the Mw6.6 earthquake. The first two tremors were felt around 22:00 and 22:30 the night before, and the third 45 minutes was before the main earthquake ([Wikipedia](https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87_%DB%B1%DB%B3%DB%B8%DB%B2_%D8%A8%D9%85)). 
- At least 29 serious aftershocks struck Bam following the main shock [Wikipedia](https://en.wikipedia.org/wiki/2003_Bam_earthquake).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                                                                                   |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Year                 | 2003                                                                                                                          |
| Country              | Iran                                                                                                                          |
| Region               | Kerman                                                                                                                        |
| Event_Name           | Bam                                                                                                                           |
| Local_Date           | 26/12/2003                                                                                                                    |
| Local_Time           | 17:26:26                                                                                                                      |
| Longitude            | 58.35                                                                                                                         |
| Latitude             | 29.09                                                                                                                         |
| Depth_(km)           | 10                                                                                                                            |
| Mw                   | 6.6                                                                                                                           |
| Max_Intensity_(MMI)  | IX                                                                                                                            |
| Fault_mechanism      | Strike Slip                                                                                                                   |
| Tectonic_region_type | Active Crustal                                                                                                                |
| Fatalities           | 25000-50000                                                                                                                   |
| Injured              | 14300-200000                                                                                                                  |
| Displaced_Population | 45000-75600                                                                                                                   |
| Affected_Population  | 142000-200000                                                                                                                 |
| Affected_Units       | nan                                                                                                                           |
| Damaged_Units        | 2381-20246 Buildings                                                                                                          |
| Collapsed_Units      | 10176-52756 Buildings                                                                                                         |
| Economic_Losses      | 32.7-1500 M USD                                                                                                               |
| Insured_Losses       | nan                                                                                                                           |
| Induced_Effects      | nan                                                                                                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000cg2d/executive                                                        |
| Wikipedia page       | https://fa.wikipedia.org/wiki/%D8%B2%D9%85%DB%8C%D9%86%E2%80%8C%D9%84%D8%B1%D8%B2%D9%87_%DB%B1%DB%B3%DB%B8%DB%B2_%D8%A8%D9%85 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
