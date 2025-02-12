# RECORDING STATIONS

![](recording_stations.png)

A unified database of recording stations is available in `Stations_Unique.csv` file.
When the same station data is found in multiple sources, the information from the highest priority source is preferred to avoid duplication.

For this particular event, the `Stations_Unique.csv` file considers the macroseismic data as reported by the USGS ShakeMap (last accessed March 2023). Other macroseismic files are available considering different source data and GMICE.

## Reference datasets

The reference datasets were used in the following priority order:

- `Stations_CESMD`: Records were downloaded from the Center for Engineering Strong Motion Data, [CESMD](http://www.strongmotioncenter.org/). Raw data in Accelerograms_CESMD.zip. Last accessed March 2023.

- `Station_DMG`: Record for DMG station was available from the online material of Bhattarai et al (2015). Bhattarai M, Adhikari LB, Gautam UP, Laurendeau A, Labonne C, Hoste-Colomer R, Sèbe O, Hernandez, B (2015). Overview of the large 25 April 2015 Gorkha, Nepal, earthquake from accelerometric perspectives. Seismological Research Letters, 86(6):1540-1548. https://doi.org/10.1785/0220150140. Last accessed March 2023.

- `Stations_USGS`: USGS Recording stations. Raw file [stationlist.json](https://earthquake.usgs.gov/product/shakemap/us20002926/atlas/1594162031303/download/stationlist.json). Last accessed March 2023.

- `Stations_MartinEtAl2015`: Macroseismic data reported in the electronic supplement of Martin SS, Hough SE and Hung C (2015) "Ground motions from the 2015 Mw 7.8 Gorkha, Nepal, Earthquake constrained by a detailed assessment of macroseismic data". Seismological Research Letters 86(6): 1524–1532. [DOI: 10.1785/0220150138](https://doi.org/10.1785/0220150138). _NOTE: Locations with intensity value "F" (felt) were removed"_.

### Use of GMICE for macroseimic data

The estimation of different IMTs for `Stations_MartinEtAl2015` made use of different GMICE, as implemented in IP notebook [1_2_stations_macroseismic_gmice](../../../src/1_stations_macroseismic_gmice.ipynb).
Values from three GMICE were compared: 

 - WardenEtAl2012: used by the USGS ShakeMap system and [Hough et al. 2016](https://doi.org/10.1007/s11069-016-2505-8) study, but derived using data from California.
 - CaprioEtAl2015: derived using global data
 - PanjamaniEtAl2017: derived for the Himalayan region (21 events)

<p align="center">
  <img src="GMICE_comparison_1.png" alt="GMICE comparison" width="600">
</p>
<p align="center">
  <img src=".GMICE_comparison_2.png" alt="GMICE comparison (log scale)" width="600">
</p>


## Notes

The event represents the first occurrence of a large continental thrust earthquake to be recorded by a high-rate (5-hertz) Global Positioning System (GPS) network very close to and completely encompassing the rupture area (Galetzka_et_al_2015.pdf). The combination of these measurements provides the opportunity to image the kinematics of the source process and the strong ground motion that led to the particular pattern of structural damage observed during this earthquake. Records of displacements and velocities were available, and they were compared to those obtained by a USGS seismic station (KATNP).

Despite being seismically active, a nationwide seismic monitoring network is not available in Nepal (Basu et al., 2021).

Some other useful references are:

- **Basu_et_al_2021:** Basu J, Podili B, Raghukanth STG, Srinagesh D (2022). Ground motion parameters for the 2015 Nepal Earthquake and its aftershocks. Natural Hazards, 1-44. https://doi.org/10.1007/s11069-022-05755-4.

- **Galetzka_et_al_2015:** Galetzka J, Melgar D, Genrich JF, Geng J, Owen S, Lindsey EO, Xu X, Bock Y, Avouac JP, Adhikari LB, Upreti BN, Pratt-Sitaula B, Bhattarai  TN, Sitaula BP, Moore A, Hudnut KW, Szeliga W, Normandeau J, Fend M, Flouzat M, Bollinger L, Shrestha P, Koirala B, Gautam U, Bhatterai M, Gupta R, Kandel T,Timsina C, Sapkota SN, Rajaure S, Maharjan N (2015). Slip pulse and resonance of the Kathmandu basin during the 2015 Gorkha earthquake, Nepal. Science, 349(6252):1091–1095. https://doi:10.1126/science.aac6383.

- **Takai_et_al_2016:** Takai N, Shigefuji M, Rajaure S, Bijukchhen S, Ichiyanagi M, Dhital MR, Sasatani T (2016). Strong ground motion in the Kathmandu Valley during the 2015 Gorkha, Nepal, earthquake. Earth, Planets and Space, 68(1):1-8. https://doi.org/10.1186/s40623-016-0383-7.
