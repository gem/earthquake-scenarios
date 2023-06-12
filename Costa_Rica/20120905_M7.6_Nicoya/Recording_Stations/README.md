# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:
- `Stations_LIS.csv`: https://www.lis.ucr.ac.cr/Descargas. Last Accesed April 2023. 
- `Stations_CRSMD.csv`: https://www.crsmd.lis.ucr.ac.cr/index.php?id=BD&pagina=51#. Last Accesed April 2023.
- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/usp000jrsw/atlas/1594175979602/download/stationlist.json). Last Accesed April 2023.


## Notes 
- `Stations_LIS_UCR`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation of specific events in the catalog prepared by the Earthquake Engineering Laboratory at the University of Costa Rica (LIS_UCR). Raw data in [`LIS_UCR_Recording_Stations.zip`](https://www.lis.ucr.ac.cr/Descargas) and [`CRSMD_LIS_UCR_Recording_Stations.zip`](https://www.crsmd.lis.ucr.ac.cr/index.php?id=BD&pagina=51#). Last accessed August 2022.