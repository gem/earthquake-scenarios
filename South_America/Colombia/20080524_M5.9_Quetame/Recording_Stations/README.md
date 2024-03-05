# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_SGC`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation prepared by the Colombian Geological Service (SGC). Raw data in [`SGC_Recording_Stations.zip`](http://bdrsnc.sgc.gov.co/paginas1/catalogo/index_rnac.php). Last accessed April 2022.
- `Stations_RAB`: RED DE ACELERÓGRAFOS DE BOGOTÁ - RAB.https://www.sire.gov.co/documents/82884/86757/InformeprocesamientoRAB2008.pdf/094cd994-0fd0-4530-ac45-9129450142ee. Last accessed June 2023.
- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/usp000g7p6/atlas/1600467315142/download/stationlist.json). Last accessed April 2022.
