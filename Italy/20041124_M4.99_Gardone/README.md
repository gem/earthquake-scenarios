# 🌎 2004 M5.1 Gardone earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2004 M5.1 Gardone earthquake in Italy.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

This is a list of earthquakes in 2004. Only earthquakes of magnitude 6 or above are included, unless they resulted in significant damage or casualties, or were notable for some other reason. All dates are listed according to UTC time. The year 2004 had the most major earthquakes since 1999. In total, there were 16 magnitude 7.0+ earthquakes this year, 6 of them were in Indonesia. Most of the earthquake deaths in 2004 were caused by the magnitude 9.1–9.3 earthquake 
off the west coast of Sumatra on December. Most of the deaths were caused by a devastating tsunami that spread across the Indian Ocean. There were several other deadly and destructive earthquakes, including Morocco's largest earthquake to date, which caused 628 deaths. Japan was hit by a magnitude 6.6 earthquake, which caused 68 deaths and $28 billion in damages, making it the fourth costliest earthquake in history.
[Wikipedia](https://en.wikipedia.org/wiki/List_of_earthquakes_in_2004)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2004                                                                   |
| Country              | Italy                                                                  |
| Region               | Gardone                                                                |
| Event_Name           | Gardone_2004                                                           |
| Local_Date           | 24/11/2004                                                             |
| Local_Time           | 22:59:40                                                               |
| Latitude             | 45.626                                                                 |
| Longitude            | 10.559                                                                 |
| Depth_(km)           | 17.2                                                                   |
| Mw                   | 5.1                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Reverse                                                                |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | nan                                                                    |
| Injured              | nan                                                                    |
| Displaced_Population | 2000-2300                                                              |
| Affected_Population  | nan                                                                    |
| Affected_Units       | 1200-4147 Buildings                                                    |
| Damaged_Units        | 500 Buildings                                                          |
| Collapsed_Units      | 40 Buildings                                                           |
| Economic_Losses      | 215 M EUR                                                              |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000d94j/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/List_of_earthquakes_in_2004              |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
