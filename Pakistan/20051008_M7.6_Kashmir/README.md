# 🌎 2005 M7.6 Kashmir earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2005 M7.6 Kashmir earthquake in Pakistan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

An earthquake occurred at 08:50:39 Pakistan Standard Time on 8 October in Azad Kashmir. It was centred near the city of Muzaffarabad, and also affected nearby Balakot in Khyber Pakhtunkhwa and some areas of Jammu and Kashmir. It registered a moment magnitude of 7.6 and had a maximum Mercalli intensity of XI (Extreme). The earthquake was also felt in Afghanistan, Tajikistan, India, and the Xinjiang region. The severity of the damage caused by the earthquake is attributed to severe upthrust. Over 86,000 people died, a similar number were injured, and millions were displaced. It is considered the deadliest earthquake in South Asia, surpassing the 1935 Quetta earthquake.
[Wikipedia](https://en.wikipedia.org/wiki/2005_Kashmir_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2005                                                                   |
| Country              | Pakistan, India, Afghanistan                                           |
| Region               | Northern Pakistan                                                      |
| Event_Name           | Kashmir                                                                |
| Local_Date           | 08/10/2005                                                             |
| Local_Time           | 08:50:39                                                               |
| Longitude            | 73.588                                                                 |
| Latitude             | 34.539                                                                 |
| Depth_(km)           | 26                                                                     |
| Mw                   | 7.6                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active shallow crustal                                                 |
| Fatalities           | 74689-88705                                                            |
| Injured              | 75277-206277                                                           |
| Displaced_Population | 2800000                                                                |
| Homeless             | 3500000-5000000                                                        |
| Affected_Population  | >5000000                                                               |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 780000 Buildings                                                       |
| Collapsed_Units      | 32335 Buildings                                                        |
| Economic_Losses      | 5000-6680 M USD                                                        |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides, rockfall, seiche                                           |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000e12e/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2005_Kashmir_earthquake                  |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
