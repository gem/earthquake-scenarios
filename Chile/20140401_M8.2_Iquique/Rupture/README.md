# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Subduction Interface |

### Preferred nodal plane solution

| source                   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:-------------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT                     |    -70.81   |   -19.7    |   21.6  |  355.053 | 15.0005 | 106    |  8.1  |
| GFZ                      |    -70.79   |   -19.58   |   34    |  346.003 | 13.0004 |  84    |  8.1  |
| Hayes_2017               |    -70.8634 |   -19.6298 |   25    |  347.006 | 13.5006 | 103.16 |  8.18 |
| IISEE_CMT                |    -70.195  |   -19.972  |   20    |  327.923 | 12.0003 |  80    |  7.95 |
| JMA                      |    -70.32   |   -19.351  |   22    |  346.002 | 14.0004 |  87    |  8.1  |
| SCARDEC                  |    -70.769  |   -19.61   |   25    |  352.029 | 23.0008 |  97    |  7.9  |
| USGS                     |    -70.7691 |   -19.6097 |   25    |  347.099 | 13.427  | 103.16 |  8.2  |
| Wei_Caltech_Iquique_2014 |    -70.817  |   -19.6423 |   21.55 |  357.062 | 18.0008 | 113.73 |  8.1  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2014&mo=4&day=1&oyr=2014&omo=4&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=8&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2022. 
- `earthquake_rupture_model_GFZ.xml`: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2014gkgf. Last accessed May 2022. 
- `earthquake_rupture_model_IISEE.xml`: International Institute of Seismology and Earthquake Engineering (IISEE). https://iisee.kenken.go.jp/eqcat/eqcatevent/201404012346.html. Last accessed May 2022. 
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20140401234646.html. Last accessed May 2022. 
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/. Last accessed May 2022. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usc000nzvd/atlas/1594162882765/download/rupture.json. Last accessed May 2022.
- `earthquake_rupture_model_Wei_Caltech_Iquique_2014.xml` and `earthquake_rupture_model_Hayes_2017.xml`:Earthquake_Source_Model_Database. http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed May 2022. 
- `IPGP.jpg`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=usc000nzvd. Last accessed May 2022.
- `IRIS.pdf`: Moment Tensor for MW 8.1 (GCMT) NEAR COAST OF NORTHERN CHILE. http://ds.iris.edu/spud/momenttensor/9647147. Last accessed May 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://isc-mirror.iris.washington.edu/cgi-bin/web-db-run?event_id=610102185&out_format=ISF2&request=COMPREHENSIVE. Last accessed May 2022. Geophysical Survey of Russian Academy of Sciences (MOS) rupture model which has been exported from ISC.pdf. 