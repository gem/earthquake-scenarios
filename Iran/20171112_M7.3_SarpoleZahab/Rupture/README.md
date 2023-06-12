# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Thrust         |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| GCMT     |     45.84   |    34.83   |    17.9 |  120.805 |  82.9999 |     82 |   7.4 |
| GFZ      |     45.9    |    34.85   |    25   |  120.832 |  77.999  |     77 |   7.3 |
| IPGP     |     45.794  |    34.93   |    19   |  124.814 |  82.9991 |     75 |   7.4 |
| IRSC     |     45.76   |    34.77   |     8   |  115.793 |  86.0015 |     81 |   7.4 |
| JMA      |     45.549  |    35.049  |    23   |  123.839 |  77.0002 |     77 |   7.3 |
| USGS     |     45.9592 |    34.9109 |    19   |  nan     | nan      |     82 |   7.3 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2017&mo=11&day=12&oyr=2017&omo=11&oday=12&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed August 2022. 
- `earthquake_rupture_model_GFZ.xml`: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2017wexs. Last accessed August 2022. 
- `earthquake_rupture_model_IPGP.xml:` The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=us2000bmcg. Last accessed February 2022.
- `earthquake_rupture_model_IRSC.xml`: Focal Mechanism (2017-11). http://irsc.ut.ac.ir/focal.php?year=2017&month=11. 
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20171112181817.html. Last accessed August 2022.
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us2000bmcg/atlas/1594400092790/download/rupture.json. Last accessed August 2022. 
- `IRIS.pdf`: Moment Tensor for MW 7.4 (GCMT) IRAN-IRAQ BORDER REGION. http://ds.iris.edu/spud/momenttensor/16387155. Last accessed August 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2017&start_month=11&start_day=12&start_time=00%3A00%3A00&end_year=2017&end_month=11&end_day=12&end_time=23%3A59%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed August 2022. 