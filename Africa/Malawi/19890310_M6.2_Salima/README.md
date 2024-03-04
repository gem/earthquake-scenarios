# 🌎 {DATE} M{MAGNITUDE} {NAME} earthquake
[[_TOC_]]

# 📂 The repository  

This repository hosts detailed information about the {DATE} M{MAGNITUDE} {NAME} earthquake in {COUNTRY}.

Available information in the folders:

- Impact
- Recording stations
- Ruptrues
- OpenQuake_gmfs 


# 🚀 The earthquake at a glance 

{WIKI_SUMMARY}
[Wikipedia]({WIKI_URL})



## Ground shaking

The estimation of the ground shaking has The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) stores the required input files to generate the ground motion fields considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, when available. The figures below present an example of the results, showing the median ground motion fields with and without conditioning the ground shaking for the rupture and ground motion model that indicates the lowest nominal bias.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

{TABLE}


# 🌟 Contributors 

We would like to acknowledge the many contributors to the Earthquake Consequence Database.
