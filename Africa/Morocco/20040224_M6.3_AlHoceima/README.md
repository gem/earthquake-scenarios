# 🌎 2004 M6.3 AlHoceima earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2004 M6.3 AlHoceima earthquake in Morocco.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 
The `2004 Al Hoceima earthquake` struck at 2:27 local time on 24 February 2004 with an estimated magnitude of Mw6.3 and violent (IX) shaking. The earthquake left 628-631 dead, 926 injured, and 12,539-15,230 displaced.
(NOAA, [Wikipedia](https://en.wikipedia.org/wiki/2004_Al_Hoceima_earthquake)). An estimated 2,539 houses had collapsed (Ait Brahim et. al. 2004). The direct economic loss was estimated to be about $400M (NatCatSERVICE, Cherif et. al. 2018).

Many of the traditional houses in rural villages were destroyed, which were often made from stones and adobe. "Unchained" masonry (i.e. concrete infill frame with a gap between the frame and infills) was often destroyed as well. In the more urban areas, less damage was experienced due to more modern construction. The town of Imzouren suffered the worst damage, including several building collapses (~30; Cherkaoui 2005).


### Type of sequence
The Al Hoceima 2004 event at 2:27 local time is considered a main shock, which was followed by hundreds of aftershocks. There were three strong aftershocks on 26 February, 2 March, and 7 March with a magnitude of Mw5.0. Those three aftershocks caused many houses that were already damaged to collapse and at least 3 more deaths (Cherkaoui 2005)


### Occurrence of other phenomena: 
Landslides and rockfall were reported between Ajdir and Beni Abdallah.


## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                            |
|:---------------------|:-----------------------------------------------------------------------|
| Year                 | 2004                                                                   |
| Country              | Morocco                                                                |
| Region               | Al Hoceima                                                             |
| Event_Name           | AlHoceima_2004                                                         |
| Local_Date           | 24/02/2004                                                             |
| Local_Time           | 02:27:47                                                               |
| Latitude             | 35.142                                                                 |
| Longitude            | 3.997                                                                  |
| Depth_(km)           | 12.2                                                                   |
| Mw                   | 6.3                                                                    |
| Max_Intensity_(MMI)  | IX                                                                     |
| Fault_mechanism      | Strike-slip; left-lateral                                              |
| Tectonic_region_type | Active Shallow Crust                                                   |
| Fatalities           | 628-631                                                                |
| Injured              | 926                                                                    |
| Displaced_Population | 12539-15230                                                            |
| Affected_Population  | nan                                                                    |
| Affected_Units       | nan                                                                    |
| Damaged_Units        | nan                                                                    |
| Collapsed_Units      | 2539 Units                                                             |
| Economic_Losses      | 300-400 M USD                                                          |
| Insured_Losses       | nan                                                                    |
| Induced_Effects      | Landslides                                                             |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/usp000cmxe/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2004_Al_Hoceima_earthquake               |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
