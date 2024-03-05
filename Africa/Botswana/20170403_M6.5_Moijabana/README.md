# 🌎 2017 M6.46 Moijabana earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2017 M6.46 Moijabana earthquake in Botswana.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2017 Moijabana earthquake` struck at 19:40 local time on 3 April 2017 with an estimated magnitude of Mw6.5 and severe (VIII) shaking in a rural area of Botswana. There are no reported deaths from this earthquake and 36 reported injuries, however the injuries were from a stampede that was triggered by the earthquake.

### Type of sequence
At least 30 M>3 events were reported following the main shock (ISC).


### Occurrence of other phenomena: 
Stampede

## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2017                                                                   |
| Country              | Botswana                                                               |
| Region               | Ghanzi                                                                 |
| Event_Name           | Moijabana_2017                                                         |
| Local_Date           | 03/04/2017                                                             |
| Local_Time           | 19:40:18                                                               |
| Latitude             | -22.6784                                                               |
| Longitude            | 25.1558                                                                |
| Depth_(km)           | 23.5                                                                   |
| Mw                   | 6.46                                                                   |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Normal                                                                 |
| Tectonic_region_type | Unknown (occurred in an area with no know previous seismicity)         |
| Fatalities           | 0                                                                      |
| Injured              | 0                                                                      |
| Displaced_Population | 271                                                                    |
| Affected_Population  | 271                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 13 Units                                                               |
| Collapsed_Units      | nan                                                                    |
| Economic_Losses      | nan                                                                    |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Stampede                                                               |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us10008e3k/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2003_Boumerd%C3%A8s_earthquake           |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
