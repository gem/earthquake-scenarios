# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_SGC`: Seismic data provided have been the product of the instrumentation and processing work of the Seismic Instrumentation prepared by the Colombian Geological Service (SGC). Raw data in [`SGC_Recording_Stations.zip`](http://bdrsnc.sgc.gov.co/paginas1/catalogo/index_rnac.php). Last accessed May 2022.
- `Stations_BMF_1999`: Strong Movement Bulletin. Sismo del Quindío, January 25, 1999. Special Volume. Accelerograms and Response Spectra. Version year 1999. data available in [`BMF_1999.PDF`](https://miig.sgc.gov.co/Paginas/Resultados.aspx?k=(FechaPublicacion%3E=1999-01-25T00:00:00Z%20AND%20FechaPublicacion%3C=1999-01-25T00:00:00Z)). Last accessed May 2022.
- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/usp00091q3/atlas/1607465655768/download/stationlist.json). Last accessed May 2022.


## Notes
There is also some additional information regarding recording stations in [`BMF_1999.PDF`](https://miig.sgc.gov.co/Paginas/Resultados.aspx?k=(FechaPublicacion%3E=1999-01-25T00:00:00Z%20AND%20FechaPublicacion%3C=1999-01-25T00:00:00Z)) and [Sarabia_and_Cifuentes_2010.pdf](http://sish.sgc.gov.co/visor/sesionServlet?metodo=irAInfoDetallada&idSismo=62#), which was covered by SGC. That is why this data has not been reported to avoid duplicates. 