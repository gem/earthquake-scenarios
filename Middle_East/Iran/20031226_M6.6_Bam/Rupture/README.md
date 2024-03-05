# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Strike Slip    |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source             |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:-------------------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| GCMT               |      58.24  |     29.1   |      15 |  172.002 |  59      |    167 |   6.6 |
| Jackson_et_al_2006 |      58.26  |     28.95  |       6 |  180.012 |  64.0015 |    150 |   6.6 |
| SCARDEC            |      58.31  |     29     |       8 |  171.996 |  73.999  |    172 |   6.5 |
| USGS               |      58.311 |     28.995 |      10 |  nan     | nan      |    167 |   6.6 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2003&mo=12&day=26&oyr=1976&omo=1&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6&umw=6.6&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023.
- `earthquake_rupture_model_Jackson_et_al_2006.xml:` Jackson, J., Bouchon, M., Fielding, E., Funning, G., Ghorashi, M., Hatzfeld, D., ... & Wright, T. (2006). Seismotectonic, rupture process, and earthquake-hazard aspects of the 2003 December 26 Bam, Iran, earthquake. Geophysical Journal International, 166(3), 1270-1292. https://www.semanticscholar.org/paper/Seismotectonic%2C-rupture-process%2C-and-aspects-of-the-Jackson-Bouchon/c5fe2b32d758de7c2fe6569f37d8a7d09f528146. Last accessed November 2022.
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are `earthquake_rupture_model_SCARDEC.xml ` therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/#. Last accessed May 2022.
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp000cg2d/atlas/1594171879053/download/rupture.json. Last accessed February 2023.
- `IRIS.pdf`: Moment Tensor for MW 6.6 (GCMT) SOUTHERN IRAN. http://ds.iris.edu/spud/momenttensor/930095. Last accessed February 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2003&start_month=12&start_day=26&start_time=00%3A00%3A00&end_year=2003&end_month=12&end_day=26&end_time=20%3A09%3A00&min_dep=&max_dep=&min_mag=6&max_mag=6.6&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed February 2023.
- `Poiata_et_al_2012`: Earthquake Source Model Database. http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1978TABASI01HART/. Rupture geometry from [SRCMOD - s2003BAMIRA01POIA.fsp](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s2003BAMIRA01POIA/). Last accessed February 2023.