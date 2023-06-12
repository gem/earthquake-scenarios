# 🌎 1992 M6.7 Erzincan earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 1992 M6.7 Erzincan earthquake in Turkey.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 13 March, at 7:19 pm, the 1992 Erzincan earthquake struck eastern Turkey with a moment magnitude of 6.7 and a maximum Mercalli intensity of VIII (Severe) [Wikipedia](https://en.wikipedia.org/wiki/1992_Erzincan_earthquake). Originating on the North Anatolian Fault, the epicentre was located less than 8 kilometers away from Erzincan's central business district. Damage was extensive both in the Erzincan district and province. Four aftershocks ranging from 5.0 to 6.1 Mw were registered according to the Ministry of Public works and settlements. [U_Colorado_Report](http://cidbimena.desastres.hn/docum/crid/Abril2006/CD2/pdf/eng/doc8863/doc8863-contenido.pdf).


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 1992                                                                   |
| Country              | Turkey                                                                 |
| Region               | Erzincan                                                               |
| Event_Name           | Erzincan                                                               |
| Local_Date           | 13/03/1992                                                             |
| Local_Time           | 17:18:39                                                               |
| Latitude             | 39.71                                                                  |
| Longitude            | 39.605                                                                 |
| Depth_(km)           | 27.2                                                                   |
| Mw                   | 6.7                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Strike-slip                                                            |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 541-653                                                                |
| Injured              | 2000-3850                                                              |
| Displaced_Population | 36000-95000                                                            |
| Affected_Population  | 250000                                                                 |
| Affected_Units       | 15042 Buildings                                                        |
| Damaged_Units        | 9227 Buildings                                                         |
| Collapsed_Units      | 5500-7007 Buildings                                                    |
| Economic_Losses      | 667-750 M USD                                                          |
| Insured_Losses       | 10.8 M USD                                                             |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000547c/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/1992_Erzincan_earthquake                 |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
