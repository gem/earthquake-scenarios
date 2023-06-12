# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.


## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_NIED`: Seismic data provided are downloaded from the National Research Institute for Earth Science and Disaster Prevention (NIED) website (https://www.bosai.go.jp/e/index.html), which notably includes stations from the KiK-net and K-net networks. Last accessed April 2023.

- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/official20110311054624120_30/atlas/1594161746661/download/stationlist.json/shakemap/stations). Last accessed April 2023.

## Notes

Strong motion datasets for past Japanese earthquakes are available from the National Research Institute for Earth Science and Disaster Prevention (NIED) website with user registration: [https://www.bosai.go.jp/e/index.html](https://www.bosai.go.jp/e/index.html).