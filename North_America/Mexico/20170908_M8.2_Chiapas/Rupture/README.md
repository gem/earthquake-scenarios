# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal fault         |
| Tectonic region type | Subduction Intraslab |

### Preferred nodal plane solution

| source                |   longitude |   latitude |   depth |   strike |     dip |    rake |   mag |
|:----------------------|------------:|-----------:|--------:|---------:|--------:|--------:|------:|
| GCMT                  |    -94.66   |    15.38   |   44.8  |  318.124 | 78.0007 |  -93    |   8.2 |
| GFZ                   |    -93.77   |    15      |   64    |  318.102 | 71.0011 |  -94    |   8.1 |
| ISC                   |    -93.8817 |    14.9411 |   51.1  |  319.258 | 78.9706 | -101.35 |   8.2 |
| JMA                   |    -94.3189 |    15.5006 |   44    |  316.114 | 73.9997 |  -95    |   8.1 |
| MOS                   |    -93.8    |    14.979  |   47    |  315.134 | 84.0003 |  -89    |   8.2 |
| Okuwaki_and_Yagi_2017 |    -94.11   |    14.85   |   18    |  316.113 | 80.9991 |  -77.55 |   8.1 |
| SCARDEC               |    -93.899  |    15.022  |   45    |  313.118 | 75.9999 |  -98    |   8.1 |
| SSN                   |    -94.11   |    14.85   |   58    |  311.142 | 84.4009 |  -94.7  |   8.2 |
| USGS                  |    -94.16   |    15.315  |   56.61 |  315.35  | 72.7097 |  -93    |   8.2 |

### Rupture figure

![](earthquake_ruptures.png)

## References
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2017&mo=9&day=8&oyr=2017&omo=9&oday=8&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=8&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2022.
- `earthquake_rupture_model_GFZ.xml`: Information available at http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2017rpdi. Last accessed May 2022.
- `earthquake_rupture_model_ISC.xml` and  `earthquake_rupture_model_MOS.xml`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?event_id=611600536&out_format=ISF2&request=COMPREHENSIVE. Last accessed May 2022. Geophysical Survey of Russian Academy of Sciences (MOS) rupture model which has been exported from ISC.pdf. 
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20170908044921.html. Last accessed May 2022.
- `earthquake_rupture_model_Okuwaki_and_Yagi_2017.xml`: Rupture geometry from [SRCMOD - s2017CHIAPA01OKUW.fsp](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s2017CHIAPA01OKUW/). Last accessed December 2022.
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/. Last accessed April 2022. 
- `earthquake_rupture_model_SSN.xml`: The SSN Focal Mechanism can be found in: http://www.ssn.unam.mx/sismicidad/reportes-especiales/ , which has been stored as `SSNMX_rep_esp_20170907_Tehuantepec_M82.pdf` in the Reference folder. Last accessed May 2022.
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us2000ar20/atlas/1594399976203/download/rupture.json. Last accessed May 2022.
- `IPGP.jpg`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=us2000ahv0. Last accessed May 2022.
- `IRIS.pdf`: Moment Tensor for MW 8.2 (GCMT) NEAR COAST OF OAXACA, MEXICO. http://ds.iris.edu/spud/momenttensor/17998415. Last accessed May 2022.


## Notes on rupture geometry

All models here use the steep, northeast-dipping nodal plane, which seems to be 
supported by the dynamic rupture and finite fault models.

Though the strike, dip and rake of the earthquake are consistently estimated 
between models, there is a minor amount of variation in the location. This may 
not be super impactful, because the epicenter is offshore, so the epicentral 
distance to urban centers may not vary dramatically.

However, there is great variation in the depth of the rupture, at least as 
given by the hypocenters in the ruptures. Most models here as well as other
high-quality sources (e.g., [Ye et al., 
2017](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017GL076085)) 
show rupture extending from about 20-70 km depth, with the centroid (location 
of maximum seismic moment release) at about 50 km. Ruptures much shallower than 
this should be treated with some skepticism.

The JMA model from the XML is striking orthogonally to the other models.  It 
was originally also in the southern hemisphere (negative latitudes) but I (RS) 
fixed it. I think whoever originally created the .xml file made some typos.  It 
should probably be redone from scratch.