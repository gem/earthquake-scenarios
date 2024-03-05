# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_Tavera_et_al_2008`: Tavera, H., Bernal, I., Strasser, F.O. et al. Ground motions observed during the 15 August 2007 Pisco, Peru, earthquake. Bull Earthquake Eng 7, 71–111 (2009). https://doi.org/10.1007/s10518-008-9083-4. data available in [Tavera_et_al_2008.pdf](https://repositorio.igp.gob.pe/handle/20.500.12816/1115). Last accessed August 2022.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/usp000fjta/atlas/1594174187091/download/stationlist.json). Last accessed August 2022.

## Notes

- `Stations_USGS` reports an outlier latitude value that was manually deleted (`STATION_ID`:UTM:(18L 060 051 10000))
- `Stations_USGS` reports an outlier latitude value that was manually deleted (`STATION_ID`:DYOBS_1)
- `Stations_USGS` reports an outlier latitude value that was manually deleted (`STATION_ID`:DYOBS_3)

