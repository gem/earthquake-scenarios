# 🌎 2021 M7.2 Haiti earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2021 M7.2 Haiti earthquake in Haiti.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

At 08:29:09 EDT on 14 August 2021, a magnitude 7.2 earthquake struck the Tiburon Peninsula in the Caribbean nation of Haiti. It had a 10-kilometre-deep (6.2 mi) hypocenter near Petit-Trou-de-Nippes, approximately 150 kilometres (93 mi) west of the capital, Port-au-Prince. Tsunami warnings were briefly issued for the Haitian coast. At least 2,248 people were confirmed killed as of 1 September 2021 and more than 12,200 injured, mostly in the Sud Department. An estimated 650,000 people were in need of assistance. At least 137,500 buildings were damaged or destroyed.It is the deadliest earthquake and deadliest natural disaster of 2021. It is also the worst disaster to strike Haiti since the 2010 earthquake. UNICEF estimates more than half a million children were affected. The Haitian Civil Protection General Directorate (DGPC) warned of a possible large humanitarian crisis resulting from the earthquake. USAID provided US $32 million in foreign aid to Haiti for reconstruction efforts following the devastating earthquake. This earthquake had the most casualties of any disaster since the 2018 Sulawesi earthquake. The economic loss from this earthquake is estimated at over 1.5 billion US dollars, nearly 10% of the country's gross domestic product.
[Wikipedia](https://en.wikipedia.org/wiki/2021_Haiti_earthquake)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2021                                                                   |
| Country              | Haiti                                                                  |
| Region               | Nippes                                                                 |
| Event_Name           | Haiti                                                                  |
| Local_Date           | 14/08/2021                                                             |
| Local_Time           | 08:29:08                                                               |
| Longitude            | -73.4822                                                               |
| Latitude             | 18.4335                                                                |
| Depth_(km)           | 10                                                                     |
| Mw                   | 7.2                                                                    |
| Max_Intensity_(MMI)  | VIII                                                                   |
| Fault_mechanism      | Oblique-reverse                                                        |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 2529-2577                                                              |
| Injured              | 12500-12763                                                            |
| Displaced_Population | 220000                                                                 |
| Affected_Population  | 702763-800000                                                          |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | 137000-137585                                                          |
| Collapsed_Units      | 53815-115000                                                           |
| Economic_Losses      | 1.60 M USD                                                             |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | nan                                                                    |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/us6000f65h/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2021_Haiti_earthquake                    |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
