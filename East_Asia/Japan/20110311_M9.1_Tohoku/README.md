# 🌎 2011 M9.1 Tōhoku earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the 2011 M9.1 Tōhoku earthquake in Japan.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

On 11 March 2011, at 14:46 JST (05:46 UTC), a Mw 9.0–9.1 undersea megathrust earthquake occurred in the Pacific Ocean, 72 km (45 mi) east of the Oshika Peninsula of the Tōhoku region. It lasted approximately six minutes, causing a tsunami. It is sometimes known in Japan as the "Great East Japan Earthquake" (東日本大震災, Higashi nihon daishinsai), among other names. The disaster is often referred to as simply 3.11 (read san ten ichi-ichi in Japanese).It was the most powerful earthquake ever recorded in Japan, and the fourth most powerful earthquake in the world since modern record-keeping began in 1900. The earthquake triggered powerful tsunami waves that may have reached heights of up to 40.5 meters (133 ft) in Miyako in Tōhoku's Iwate Prefecture, and which, in the Sendai area, traveled at 700 km/h (435 mph) and up to 10 km (6 mi) inland. Residents of Sendai had only eight to ten minutes of warning, and more than a hundred evacuation sites were washed away. The snowfall which accompanied the tsunami and the freezing temperature hindered rescue works greatly; for instance, Ishinomaki, the city with most deaths, was 0 °C (32 °F) as the tsunami hit. The official figures released in 2021 reported 19,759 deaths, 6,242 injured, and 2,553 people missing, and a report from 2015 indicated 228,863 people were still living away from their home in either temporary housing or due to permanent relocation.The tsunami caused the Fukushima Daiichi nuclear disaster, primarily the meltdowns of three of its reactors, the discharge of radioactive water in Fukushima and the associated evacuation zones affecting hundreds of thousands of residents. Many electrical generators ran out of fuel. The loss of electrical power halted cooling systems, causing heat to build up. The heat build-up caused the generation of hydrogen gas. Without ventilation, gas accumulated within the upper refueling hall and eventually exploded causing the refueling hall's blast panels to be forcefully ejected from the structure. Residents within a 20 km (12 mi) radius of the Fukushima Daiichi Nuclear Power Plant and a 10 km (6.2 mi) radius of the Fukushima Daini Nuclear Power Plant were evacuated.
[Wikipedia](https://en.wikipedia.org/wiki/2011_Tōhoku_earthquake_and_tsunami)



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| FIELD                | DESCRIPTION                                                                              |
|:---------------------|:-----------------------------------------------------------------------------------------|
| Year                 | 2011                                                                                     |
| Country              | Japan                                                                                    |
| Region               | Tōhoku                                                                                   |
| Event_Name           | Tōhoku_2011                                                                              |
| Local_Date           | 11/03/2011                                                                               |
| Local_Time           | 14:46:18                                                                                 |
| Longitude            | 142.373                                                                                  |
| Latitude             | 38.297                                                                                   |
| Depth_(km)           | 29                                                                                       |
| Mw                   | 9.1                                                                                      |
| Max_Intensity_(MMI)  | VIII                                                                                     |
| Fault_mechanism      | Thrust/reverse                                                                           |
| Tectonic_region_type | Subduction interface                                                                     |
| Fatalities           | 13135-22312                                                                              |
| Injured              | 5314-6242                                                                                |
| Displaced_Population | 130927-500000                                                                            |
| Affected_Population  | 368820                                                                                   |
| Affected_Units       | >332395                                                                                  |
| Damaged_Units        | 144300-280920                                                                            |
| Collapsed_Units      | 121778-400000                                                                            |
| Economic_Losses      | 169000-360000 M USD                                                                      |
| Insured_Losses       | 37500 M USD                                                                              |
| Induced_Effects      | Tsunami                                                                                  |
| USGS page            | https://earthquake.usgs.gov/earthquakes/eventpage/official20110311054624120_30/executive |
| Wikipedia page       | https://en.wikipedia.org/wiki/2011_Tōhoku_earthquake_and_tsunami                         |


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
