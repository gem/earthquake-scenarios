# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description               |
|:---------------------|:--------------------------|
| Fault mechanism      | Right-lateral strike slip |
| Tectonic region type | Active Shallow Crustal    |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth | strike   | dip   |   rake |   mag |
|:---------|------------:|-----------:|--------:|:---------|:------|-------:|------:|
| GCMT     |     134.99  |    34.78   |    20.3 | 230.13   | 79.0  |    160 |   6.9 |
| ISC      |     135.018 |    34.583  |    15   | 233.11   | 90.0  |    163 |   6.8 |
| JMA      |     135.21  |    34.359  |    16   | 229.12   | 82.0  |    172 |   6.9 |
| SCARDEC  |     135.02  |    34.58   |    14   | 232.13   | 71.0  |    162 |   6.9 |
| USGS     |     134.931 |    34.5325 |    10   |          |       |    172 |   6.9 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1995&mo=1&day=16&otype=ymd&oyr=1995&omo=1&oday=17&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=6.5&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `ISC.pdf`: International Seismological Centre (ISC), On-Line Bulletin. Available online at: http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=1995&start_month=1&start_day=16&start_time=00%3A00%3A00&end_year=1995&end_month=1&end_day=17&end_time=00%3A00%3A00&min_dep=&max_dep=&min_mag=6&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_ISC.xml`.

- `JMA.pdf`: Japan Meteorological Agency (JMA). Available online at: https://www.data.jma.go.jp/eqev/data/mech/pdf/cmt1995.pdf. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_JMA.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at: http://scardec.projects.sismo.ipgp.fr. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/usp0006rew/atlas/1594167475099/download/rupture.json. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.
