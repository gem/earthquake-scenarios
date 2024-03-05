# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Subduction Interface |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| AUST     |    -99.6933 |    17.033  |    11.5 |  115.755 |  42.4299 | 106.42 |  6.8  |
| GCMT     |    -99.76   |    17.03   |    21.8 |  116.951 |  69.9984 |  96    |  7    |
| GFZ      |    -99.74   |    16.97   |    22   |  117.95  |  74.998  |  93    |  7    |
| IPGP     |    -99.788  |    16.95   |    15   |  113.941 |  68.9997 | 101    |  7.11 |
| JMA      |    -99.425  |    17.087  |    21   |  111.946 |  72.0019 |  93    |  7    |
| SSN      |    -99.78   |    16.82   |    10   |  109.438 |  77.299  |  90.3  |  7.1  |
| USGS     |    -99.7429 |    16.9722 |    20   |  nan     | nan      |  96    |  7    |

### Rupture figure

![](earthquake_ruptures.png)

## References
- `earthquake_rupture_model_AUST.xml`: Geoscience Australia (AUST). https://earthquakes.ga.gov.au/event/ga2021evbvpw. Last accessed June 2022.
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2021&mo=09&day=08&oyr=2021&omo=09&oday=08&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed June 2022.
- `earthquake_rupture_model_GFZ.xml`: **GFZ.txt** and **GFZ.pdf** available at http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2021roxi. Last accessed June 2022.
- `earthquake_rupture_model_IPGP.xml`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=us7000f93v. Last accessed June 2022.
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20210908014747.html. Last accessed June 2022.
- `earthquake_rupture_model_SSN.xml`: The SSN Focal Mechanism available at http://www.ssn.unam.mx/sismicidad/reportes-especiales/, report available as `SSNMX_rep_esp_20210907_Guerrero_M71` in the Reference folder. Last accessed June 2022.
- `earthquake_rupture_model_USGS.xml`: from `USGS.json` rupture. https://earthquake.usgs.gov/product/shakemap/us7000f93v/us/1632532448210/download/rupture.json. Last accessed June 2022.
- `IRIS.pdf`: Moment Tensor for MW 7.0 (GCMT) GUERRERO, MEXICO. http://ds.iris.edu/spud/momenttensor/19759038. Last accessed June 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=2021&start_month=9&start_day=08&start_time=00%3A00%3A00&end_year=2021&end_month=9&end_day=08&end_time=23%3A59%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed June 2022. 