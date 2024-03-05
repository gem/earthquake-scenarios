# 🌎 2015 M6.5 Lefkada earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2015 M6.5 Lefkada earthquake in Greece.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

The 2015 Lefkada earthquake occurred on November 17, 2015, 10:40:07 (EEST) with a moment magnitude of 6.5 located 19 km Southwest of the Greek island of Lefkada along with a depth of 11 km and intensities reaching as high as VIII (Severe) on the Modified Mercalli Scale. Two people lost their lives in the event and 4–8 others were hospitalized with injuries. Significant secondary effects like landslides, rock falls, road cracks, ground subsidence, liquefaction, which where the cause of the major losses
[Wikipedia](https://en.wikipedia.org/wiki/2015_Lefkada_earthquake) and 
[Academic article](https://members.noa.gr/aganas/en/Paper_ICOHNIC2016_006.pdf)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2015                                                                   |
| Country              | Greece                                                                 |
| Region               | Lefkada                                                                |
| Event_Name           | Lefkada_2015                                                           |
| Local_Date           | 17/11/2015                                                             |
| Local_Time           | 07:10:07                                                               |
| Latitude             | 38.67                                                                  |
| Longitude            | 20.6                                                                   |
| Depth_(km)           | 11                                                                     |
| Mw                   | 6.5                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 0-2                                                                    |
| Injured              | 4-10                                                                   |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 1 Buildings                                                            |
| Economic_Losses      | 20 M USD                                                               |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, rock falls, road cracks, ground subsidence, liquefaction   |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10003ywp/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2015_Lefkada_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
