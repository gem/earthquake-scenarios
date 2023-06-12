# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_IGEPN`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation of specific events in the catalog prepared by Instituto Geofísico Escuela Politécnica Nacional (IGEPN). Raw data in [`IGEPN_Recording_Stations`](https://www.igepn.edu.ec/registros-acelerograficos/formulario-registros-acelerograficos). Last accessed July 2022.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/us20005j32/atlas/1594162309877/download/stationlist.json). Last accessed July 2022.