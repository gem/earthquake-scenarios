# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description            |
|:---------------------|:-----------------------|
| Fault mechanism       | Oblique thrust         |
| Tectonic region type | Active shallow crustal |


### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT     |     172.52  |    -43.6   |    12   |  59.068  | 59.0056 |    147 |  6.1  |
| GFZ      |     172.81  |    -43.45  |    10   |  59.0918 | 50.9975 |    146 |  6.3  |
| SCARDEC  |     172.68  |    -43.58  |     6   |  62.0809 | 58.9997 |    138 |  6.2  |
| USGS     |     172.691 |    -43.541 |     3.7 |  56.0919 | 61.0022 |    147 |  6.35 |


### Rupture figure

![](earthquake_ruptures.png)


## References

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2011&mo=2&day=21&otype=ymd&oyr=2011&omo=2&oday=21&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=6&umw=6.1&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `GFZ.pdf`: GeoForschungsZentrum (FFZ). GEOFON Earthquake Information Service. Available online at: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2011dqyh. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GFZ.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at: http://scardec.projects.sismo.ipgp.fr/#. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/usp000huvq/atlas/1594175310841/download/rupture.json. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.


