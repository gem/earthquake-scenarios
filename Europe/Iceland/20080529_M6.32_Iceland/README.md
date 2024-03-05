# 🌎 2008 M6.3 Iceland earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2008 M6.3 Iceland earthquake in Iceland.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

South Iceland is an active seismic zone. In May 2008 a Mw6.3 earthquake struck the Ölfus region in South Iceland. The recorded maximum PGA was 0.88g. A great deal of damage occurred but fortunately there was no loss of life
[Bessason et al. 2012](https://www.iitk.ac.in/nicee/wcee/article/WCEE2012_2384.pdf)


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2008                                                                   |
| Country              | Iceland                                                                |
| Region               | Iceland                                                                |
| Event_Name           | Iceland_2008                                                           |
| Local_Date           | 29/05/2008                                                             |
| Local_Time           | 15:46:00                                                               |
| Latitude             | 64.005                                                                 |
| Longitude            | -21.013                                                                |
| Depth_(km)           | 9                                                                      |
| Mw                   | 6.3                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | nan                                                                    |
| Injured              | 0-30                                                                   |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 30 Buildings                                                           |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000g826/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2000_Iceland_earthquakes                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
