# GROUND MOTION FIELDS USING OPENQUAKE

This folder includes the OpenQuake input files to generate scenario ground motion 
fields considering different sources of information:

1. From rupture
1. From rupture and conditioned to recording stations with only seismic stations or with seismic and macroseismic stations
1. From ShakeMap


## Median ground motion fields

The following images present the median ground motion field for the combination of rupture and GMPE that generates the lowest `nominal bias`, when conditioning the ground shaking to information from the recording stations. The folder [Sensitivity](./Sensitivity/) provides the summary of the sensitivity analysis carried out with the available ruptures and GMPEs.

<img src="gmf_median_no_stations.png" height="250">
<img src="gmf_median_with_stations_all.png" height="250">
<img src="gmf_median_with_stations_seismic.png" height="250">


### 1. From Rupture

Start a calculation from a given rupture in OpenQuake xml format and combine it with a 
logic tree for the applicable GMPEs (ground motion prediction equations)

```
rupture + gmpe_logic_tree + job_no_stations.ini
```


### 2. From Rupture and conditional to recording stations

Condition the ground motion fields based on the recording stations available for the event
(`stationlist.csv` files). In this case the calculation uses a given rupture in 
OpenQuake xml format, the observed values in the recording stations, and a given ground
motion model.

The conditioning of the ground motion considers:
- All recording stations (with seismic and macroseismic values).
- The recording stations with only seismic stations.

```
rupture + gmpe_logic_tree + stationlist_all.csv + job_with_stations_all.ini
rupture + gmpe_logic_tree + stationlist_seismic.csv + job_with_stations_seismic.ini
```


### 3. From Shakemap

The gmfs computed from the USGS ShakeMap can be generated with the command

```
oq shakemap2gmfs {shakemap_id} {sites.csv} -n 0 -s 0 -t 0 --spatialcorr yes -c yes

example of shakemap_id: us2000ar20 
```

It is possible to specify the number of ground motion fields, the truncation level,
the spatial correlation and the cross-correlation.

In OpenQuake, it is also possible to run scenario risk calculations starting from the USGS
ShakeMap.

