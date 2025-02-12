# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description            |
|:---------------------|:-----------------------|
| Fault mechanism      | Strike slip            |
| Tectonic region type | Active shallow crustal |


### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT     |     172.12  |    -43.56  |      12 |  88.2518 | 88.9982 |    172 |     7 |
| JMA      |     172.072 |    -43.318 |       5 |  86.2502 | 86.9979 |    153 |     7 |
| SCARDEC  |     171.83  |    -43.52  |       9 |  89.2515 | 77.0035 |    171 |     7 |


### Rupture figure

![](earthquake_ruptures.png)


## References

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2010&mo=9&day=3&otype=ymd&oyr=2010&omo=9&oday=4&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=6.6&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `JMA.pdf`: Japan Meteorological Agency (JMA). Available online at: https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20100904013546.html. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_JMA.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at:  http://scardec.projects.sismo.ipgp.fr. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/us20002926/atlas/1594162031303/download/rupture.json. Last accessed May 2023.
