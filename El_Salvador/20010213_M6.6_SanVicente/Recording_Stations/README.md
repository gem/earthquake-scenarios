# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_MARN`: Filtered stations from MARN. 

- `Stations_Casado_et_al_2001`: Casado, C. & Benito, Belén & Bommer, Julian & Ciudad, M. & Peláez, José. (2001). ANÁLISIS DE LOS ACELEROGRAMAS REGISTRADOS EN LOS TERREMOTOS DE EL SALVADOR DE 2001. data available in [Casado_et_al_2001.pdf](https://www.researchgate.net/publication/251945282_ANALISIS_DE_LOS_ACELEROGRAMAS_REGISTRADOS_EN_LOS_TERREMOTOS_DE_EL_SALVADOR_DE_2001). Last accessed July 2022.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/usp000a9jv/atlas/1594170340990/download/stationlist.json). Last accessed July 2022.


## Notes

- The `Stations_Unique.csv` file only uses the stations reported by MARN, as it is the official source in the country and it has been post-processed and filtered.

- **MARN:** El Salvador National Seismic Network. The Ministry of Environment and Natural Resources (Ministerio del Medio Ambiente y Recursos Naturales, MARN). http://www.snet.gob.sv/ver/sismologia/estudios/. Last accessed January 2024. 
