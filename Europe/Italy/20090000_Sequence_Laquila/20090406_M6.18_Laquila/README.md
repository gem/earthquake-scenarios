# 🌎 2009 M6.3 Laquila earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2009 M6.3 Laquila earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2009 L'Aquila earthquake occurred in the region of Abruzzo, in central Italy. The main shock occurred at 03:32 CEST (01:32 UTC) on 6 April 2009, and was rated 5.8 or 5.9 on the Richter magnitude scale and 6.3 on the moment magnitude scale; its epicentre was near L'Aquila, the capital of Abruzzo, which together with surrounding villages suffered the most damage. There have been several thousand foreshocks and aftershocks since December 2008, more than thirty of which had a Richter magnitude greater than 3.5.The earthquake was felt throughout central Italy; 308 people are known to have died, making this the deadliest earthquake to hit Italy since the 1980 Irpinia earthquake. In a subsequent inquiry of the handling of the disaster, seven members of the Italian National Commission for the Forecast and Prevention of Major Risks were accused of giving "inexact, incomplete and contradictory" information about the danger of the tremors prior to the main quake. On 22 October 2012, six scientists and one ex-government official were convicted of multiple manslaughter for downplaying the likelihood of a major earthquake six days before it took place. They were each sentenced to six years' imprisonment, but the verdict was overturned on 10 November 2014. Criticism was also applied to poor building standards that led to the failure of many modern buildings in a known earthquake zone: an official at Italy's Civil Protection Agency, Franco Barberi, said that "in California, an earthquake like this one would not have killed a single person".
[Wikipedia](https://en.wikipedia.org/wiki/2009_L%27Aquila_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2009                                                                   |
| Country              | Italy                                                                  |
| Region               | Laquila                                                                |
| Event_Name           | Laquila_2009                                                           |
| Local_Date           | 06/04/2009                                                             |
| Local_Time           | 01:32:39                                                               |
| Latitude             | 42.334                                                                 |
| Longitude            | 13.334                                                                 |
| Depth_(km)           | 8.8                                                                    |
| Mw                   | 6.3                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Active Shallow Crust                                                   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000gvtu/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2009_L%27Aquila_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
