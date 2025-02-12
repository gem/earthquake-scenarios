# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description            |
|:---------------------|:-----------------------|
| Fault mechanism      | Thrust/reverse         |
| Tectonic region type | Subduction interface   |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GMCT     |     143.05  |    37.52   |   20    |  204.469 | 10.0053 |     88 |   9.1 |
| JMA      |     142.516 |    38.62   |   24    |  193.975 | 10.004  |     79 |   9   |
| NIED     |     142.861 |    38.1035 |   23.74 |  201.177 | 27.0095 |     88 |   9   |
| SCARDEC  |     142.37  |    38.3    |   15    |  198.108 | 14.0055 |     84 |   9   |
| USGS     |     142.373 |    38.297  |   29    |  195.341 | 12.0712 |     79 |   9.1 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2011&mo=3&day=11&otype=ymd&oyr=2011&omo=3&oday=11&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=9&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `JMA.pdf`: Japan Meteorological Agency (JMA). Available online at: https://www.data.jma.go.jp/eqev/data/mech/pdf/cmt2011.pdf. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_JMA.xml`.

- `NIED.pdf`: National Research Institute for Earth Science and Disaster Prevention (NIED). Broadband Seismograph Network. Available online at: https://www.fnet.bosai.go.jp/event/joho.php?tm=201103&LANG=en&VIEW=50&TSORT=asc. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_NIED.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at:  http://scardec.projects.sismo.ipgp.fr. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/official20110311054624120_30/atlas/1594161746661/download/rupture.json. Last accessed April 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.