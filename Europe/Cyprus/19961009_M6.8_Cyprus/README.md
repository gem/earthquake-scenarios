# 🌎 1996 M6.8 Cyprus earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1996 M6.8 Cyprus earthquake in Cyprus.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 9 October 1996, a very strong earthquake measuring 6.8 occurred in the southwestern part of Cyprus. It caused panic among the residents of Paphos and Limassol and tenants of apartment buildings in Nicosia, Larnaca and Paralimni. Two people died, and 20 were slightly injured. Limited damage was caused.
[News article](https://www.financialmirror.com/2022/01/11/cyprus-quake-strongest-since-1996/#:~:text=On%209%20October%201996%2C%20a,and%2020%20were%20slightly%20injured)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1996                                                                   |
| Country              | Cyprus                                                                 |
| Region               | Cyprus                                                                 |
| Event_Name           | Cyprus                                                                 |
| Local_Date           | 09/10/1996                                                             |
| Local_Time           | 13:10:52                                                               |
| Latitude             | 34.556                                                                 |
| Longitude            | 32.126                                                                 |
| Depth_(km)           | 33                                                                     |
| Mw                   | 6.8                                                                    |
| Max_Intensity_(MMI)  | VI                                                                     |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 0-2                                                                    |
| Injured              | 0-5                                                                    |
| Displaced_Population | nan                                                                    |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 570.0 Buildings                                                        |
| Collapsed_Units      | 70.0 Buildings                                                         |
| Economic_Losses      | 0-4.34 M USD                                                           |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp0007r4u/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2020_Petrinja_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
