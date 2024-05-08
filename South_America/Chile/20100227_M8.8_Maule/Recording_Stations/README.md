# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.

## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_Informe_UCH_2010_And_Boroschek_et_al_2012`: Efemérides Sísmicas: Terremoto del Maule 2010. data available in [Informe_UCH_2010.pdf](http://www.terremotosuchile.cl/red_archivos/RENAMAULE2010R2.pdf) and [`Boroschek_et_al_2012.pdf`](https://journals.sagepub.com/doi/10.1193/1.4000045). Last accessed August 2022.
- `Stations_Verdugoa_et_al_2018`: Verdugo, Ramon & Ochoa-Cornejo, Felipe & Gonzalez, Javiera & Valladares, Guillermo. (2018). Site effect and site classification in areas with large earthquakes. Soil Dynamics and Earthquake Engineering. 126. https://doi.org/10.1016/j.soildyn.2018.02.002. data available in [Verdugoa_et_al_2018.pdf](../../References/Verdugoa_et_al_2018.pdf). Last accessed August 2022.
- `Stations_MAE_Center_Report`: The Maule (Chile) Earthquake of February 27, 2010. data available in [MAE_Center_Report.pdf](https://core.ac.uk/download/pdf/4826647.pdf). Last accessed August 2022.
- `Stations_USGS`: USGS Recording stations. Raw file [`stationlist.json`](https://earthquake.usgs.gov/product/shakemap/official20100227063411530_30/atlas/1594161725779/download/stationlist.json). Last accessed August 2022.


## Notes

- `Stations_USGS` reports an outlier macroseismic value that was manually deleted (`STATION_ID`:UTM:(19H -38 865 10000)). In addition, the macroseismic values reported for `OBS_78` (in Sao Paulo) and `OBS_35` (Lima).