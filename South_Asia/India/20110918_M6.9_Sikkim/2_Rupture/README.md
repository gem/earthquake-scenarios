# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism      | Strike-slip          |
| Tectonic region type | Subduction intraslab |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |   dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|------:|-------:|------:|
| GCMT     |      88.35  |      27.44 |      46 |   310.09 |    79 |   -162 |   6.9 |
| ISC      |      87.97  |      27.53 |      60 |   308.09 |    86 |   -164 |   6.9 |
| SCARDEC  |      88.15  |      27.73 |      61 |   312.09 |    84 |   -166 |   6.9 |
| USGS     |      88.155 |      27.73 |      50 |   310.09 |    79 |   -162 |   6.9 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2011&mo=9&day=18&oyr=1976&omo=1&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6.5&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `ISC.pdf`: International Seismological Centre (ISC), On-Line Bulletin. Available online at: http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=2011&start_month=9&start_day=18&start_time=00%3A00%3A00&end_year=2011&end_month=9&end_day=19&end_time=00%3A00%3A00&min_dep=&max_dep=&min_mag=6.5&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_ISC.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at: http://scardec.projects.sismo.ipgp.fr/#. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/usp000j88b/atlas/1600710324699/download/rupture.json. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.