# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`]https://earthquake.usgs.gov/product/shakemap/us7000kp2i/us/1692303340170/download/stationlist.json/shakemap/stations. Last accessed 18 August 2023.

- `Stations_SGC`: Seismic Instrumentation processed by the Colombian Geological Service (SGC). Raw data in [SGC_station_data.csv](https://sismo.sgc.gov.co/evento/SGC2023qdvnvf). Last accessed 18 August 2023.
- `stationlist_SGC.json`: Colombian Geological Service (SGC). https://archive.sgc.gov.co/events/SGC2023qelupa/mmi/stationlist.json. Last accessed 18 August 2023.

## Notes
