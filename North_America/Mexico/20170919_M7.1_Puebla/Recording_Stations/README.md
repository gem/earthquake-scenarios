# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Station_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_UNAM`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation Unit at the Instituto de Ingenieria of the National Autonomous University of Mexico (UNAM). Raw data in [`Accelerogram_RAII_UNAM.zip`](http://aplicaciones.iingen.unam.mx/AcelerogramasRSM/) . Last accessed April 2022.

- `Stations_CDMX_GEO_DATA_And_Cires`: [Geotechnical map of CDMX](https://google.com/maps/d/embed?mid=1d0JXBfIZIUZJebf3uFQAMz181D8). Raw data in `CDMX_GEO_DATA.csv ` and [`Cires.csv`](http://www.cires.org.mx/racm_mapainteractivo/). Last accessed April 2022.

- `Stations_Guillermo_Diaz_Fanas_2020_And_Cires`: data available in [`Guillermo_Diaz_Fanas_et_al_2020.pdf`](https://journals.sagepub.com/doi/full/10.1177/8755293020964828) and [`Cires.csv`](http://www.cires.org.mx/racm_mapainteractivo/). Last accessed April 2022.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/earthquakes/eventpage/us2000ar20/shakemap/intensity). Last accessed April 2022.


## Notes

The SSN (NATIONAL SEISMOLOGICAL SERVICE) recording stations coordinates are available in http://www.ssn.unam.mx/acerca-de/estaciones/. Last accessed April 2022.
