# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Thrust/reverse |
| Tectonic region type | Subduction     |

### Preferred nodal plane solution

| source    |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:----------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT      |     85.33   |    27.91   |   12    |  287.297 | 6.00012 |  96    |  7.9  |
| GFZ       |     84.72   |    28.18   |   18    |  304.198 | 4.00011 | 112    |  7.8  |
| Hayes     |     84.65   |    28.13   |   15    |          |         | 102.13 |  7.82 |
| IPGP      |     84.725  |    28.165  |   29    |  323.107 | 7.00003 | 133    |  7.8  |
| IRIS      |     84.731  |    28.231  |    8.22 |  287.263 | 6.0001  |  96    |  7.8  |
| ISC       |     84.725  |    28.165  |   29    |  323.107 | 7.00003 | 133    |  7.8  |
| JMA       |     85.194  |    27.54   |   12    |  299.246 | 6.00001 | 112    |  7.9  |
| Kobayashi |     84.7079 |    28.1473 |   15    |          |         |  98.37 |  7.84 |
| SCARDEC   |     84.731  |    28.23   |   12    |  301.244 | 6.00011 | 111    |  7.9  |
| USGS      |     84.7314 |    28.2305 |    8.2  |          |         | 102.13 |  7.8  |
| Yagi      |     84.708  |    28.147  |   15    |          |         |  89.29 |  7.9  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `EQUAKE_Hayes.pdf`: Hayes, G. P., Briggs, R. W., Barnhart, W. D., Yeck, W. L., McNamara, D. E., Wald, D. J., ... & Samsonov, S. V. (2015). Rapid characterization of the 2015 M w 7.8 Gorkha, Nepal, earthquake sequence and its seismotectonic context. Seismological Research Letters, 86(6), 1557-1567. https://doi.org/10.1785/0220150145. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Hayes.xml`.

- `EQUAKE_Kobayashi.pdf`: Kobayashi, T., Morishita, Y., & Yarai, H. (2015). Detailed crustal deformation and fault rupture of the 2015 Gorkha earthquake, Nepal, revealed from ScanSAR-based interferograms of ALOS-2. Earth, Planets and Space, 67(1), 1-13. https://doi.org/10.1186/s40623-015-0359-z. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Kobayashi.xml`.

- `EQUAKE_Yagi.pdf`: Yagi, Y., & Okuwaki, R. (2015). Integrated seismic source model of the 2015 Gorkha, Nepal, earthquake. Geophysical Research Letters, 42(15), 6229-6235. https://doi.org/10.1002/2015GL064995. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Yagi.xml`.

- `GCMT.pdf`: Global Centroid Moment Tensor (GCMT) Catalog. Available online at: https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2015&mo=04&day=25&otype=ymd&oyr=2015&omo=04&oday=25&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GCMT.xml`.

- `GFZ.pdf`: GeoForschungsZentrum (FFZ). GEOFON Earthquake Information Service. Available online at: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2015iatp. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_GFZ.xml`.

- `IPGP.jpg`: Institut de Physique du Globe de Paris (IPGP). Available online at: http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=us20002926. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_IPGP.xml`.

- `IRIS.pdf`: IRIS Data Services. Reference from GCMT. Available online at: https://ds.iris.edu/spud/momenttensor/10044385. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_IRIS.xml`.

- `ISC.pdf`: International Seismological Centre (ISC), On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=2015&start_month=4&start_day=25&start_time=2%3A00%3A00&end_year=2015&end_month=4&end_day=25&end_time=6%3A30%3A00&min_dep=&max_dep=&min_mag=&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_ISC.xml`.

- `JMA.pdf`: Japan Meteorological Agency (JMA). Available online at: https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20150425061126.html. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_JMA.xml`.

- `SCARDEC.pdf`: SCARDEC, Source Time Functions (STFs) database. Available online at: http://scardec.projects.sismo.ipgp.fr/#. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_SCARDEC.xml`.

- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/us20002926/atlas/1594162031303/download/rupture.json. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.
