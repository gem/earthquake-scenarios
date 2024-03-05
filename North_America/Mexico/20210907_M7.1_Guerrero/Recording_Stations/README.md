# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_UNAM`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation Unit at the Instituto de Ingenieria of the National Autonomous University of Mexico (UNAM). Raw data in [`Accelerogram_RAII_UNAM.zip`](http://aplicaciones.iingen.unam.mx/AcelerogramasRSM/) . Last accessed April 2022.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/us7000f93v/us/1632532448210/download/rupture.json). Last accessed April 2022.


## Notes

- `Cires.csv`: On this online database, you only have accessibility to the name of some recording stations, maximum acceleration, and seismic zonation. This database does not present the coordinates of the recording stations. Raw data in http://www.cires.org.mx/racm_mapainteractivo/. Last accessed April 2022.
- The National Seismological Service (SSN) recording stations coordinates are available in http://www.ssn.unam.mx/acerca-de/estaciones/. Last accessed April 2022.