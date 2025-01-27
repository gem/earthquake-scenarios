# 🌎 2009 M6.3 Laquila earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M6.9 Sikkim earthquake in India.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2009 L'Aquila earthquake sequence` struck the Abruzzo region of central Italy, with the main shock occurring on 6 April 2009 at 03:32 local time. This earthquake had a magnitude of 6.3 and reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. The epicenter was located near L'Aquila, and the event was followed by numerous foreshocks and aftershocks, which significantly exacerbated the damage and complicated subsequent rescue efforts. A second major earthquake in the sequence struck on 7 April 2009 at 19:47 local time. With a magnitude of 5.5, this aftershock occurred in the same general area near L'Aquila, further intensifying the destruction by damaging already weakened structures and impeding relief operations.The most severely affected areas included L'Aquila and surrounding towns such as Onna, Paganica, San Gregorio, and Castelnuovo. The earthquake sequence resulted in over 295 fatalities, more than 1000 injuries, and left many individuals homeless. The economic losses were estimated at approximately 2500 million USD. In addition to the widespread structural damage, landslides were reported in the region’s mountainous areas, although there were no instances of liquefaction or tsunamis. The event underscored the significant vulnerabilities of both historical and modern structures in earthquake-prone regions, highlighting the need for enhanced seismic preparedness and disaster response strategies.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2009 |
| Country | Italy |
| Region | Europe |
| Event Name | Laquila 2009 |
| Local Date | 06/04/2009 |
| Local Time | 03:32:39 |
| Latitude (decimal degrees) | 42.334 |
| Longitude (decimal degrees) | 13.334 |
| Depth (km) | 8.8 |
| Mw | 6.3 |
| Max Intensity (MMI) | X |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000gvtu |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 295-309 |
| Injured | 1000-1500 |
| Displaced population | 55000-80000 |
| Affected population | ~56000 |
| Affected units | 35379 Buildings |
| Damaged units | 23403 Buildings |
| Collapsed units | 15000 Buildings |
| Economic losses | 2500 M USD |
| Insured losses | 260 M USD |
| Earthquake-triggered effects | nan |