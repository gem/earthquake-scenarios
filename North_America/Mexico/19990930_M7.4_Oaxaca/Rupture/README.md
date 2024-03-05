# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal fault         |
| Tectonic region type | Subduction Intraslab |

### Preferred nodal plane solution

| source               |   longitude |   latitude |   depth |   strike |     dip |     rake |   mag |
|:---------------------|------------:|-----------:|--------:|---------:|--------:|---------:|------:|
| GCMT                 |     -96.96  |     16.2   |    46.8 |  282.09  | 41.9994 | -78      |  7.4  |
| Hernandez_et_al_2001 |     -97.02  |     16     |    39.7 |  295.094 | 49.9824 | -86.9413 |  7.47 |
| USGS                 |     -96.931 |     16.059 |    60.6 |  300.072 | 60.0009 | -80      |  7.5  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1999&mo=9&day=30&oyr=1999&omo=9&oday=30&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7.4&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed July 2022. 
- `earthquake_rupture_model_Hernandez_et_al_2001_xml`: Rupture history of September 30, 1999 intraplate earthquake of Oaxaca, Mexico (MW=7.5) from inversion of strongmotion data. Geophysical Research Letters, 2001, 28, pp.363-366. https://hal-insu.archives-ouvertes.fr/insu-03606674/document. Last accessed December 2022. Rupture geometry available in [SRCMOD](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1999OAXACA01HERN/). Rupture geometry from [SRCMOD - s1999OAXACA01HERN.fsp](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1999OAXACA01HERN/).
- `earthquake_rupture_model_USGS.xml`: USGS rupture.https://earthquake.usgs.gov/product/shakemap/usp0009f7v/atlas/1594169514425/download/rupture.json. Last accessed July 2022. 
- `IRIS.pdf`: Moment Tensor for MW 7.4 (GCMT) OAXACA, MEXICO. http://ds.iris.edu/spud/momenttensor/908200. Last accessed July 2022. _NOTE: same nodal plane solution as GCMT_.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=1999&start_month=9&start_day=30&start_time=00%3A00%3A00&end_year=1999&end_month=9&end_day=30&end_time=23%3A00%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed July 2022.