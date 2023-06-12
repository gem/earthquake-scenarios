# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Subduction Intraslab |

### Preferred nodal plane solution

| source                    |   longitude |   latitude |   depth |    strike |      dip |   rake |   mag |
|:--------------------------|------------:|-----------:|--------:|----------:|---------:|-------:|------:|
| GCMT                      |    -72.09   |   -31.13   | 17.4    |   7.24414 |  19.0011 | 109    |  8.3  |
| GFZ                       |    -71.57   |   -31.52   | 23      | 358.127   |  19.0009 |  92    |  8.2  |
| Hayes_2017                |    -71.57   |   -31.52   | 23      |   6.11537 |  19.1506 | 100.87 |  8.23 |
| JMA                       |    -71.453  |   -31.388  | 28      |   3.20347 |  14.001  |  99    |  8.3  |
| Matthew_Herman_et_al_2017 |    -71.6728 |   -31.5953 | 25.4471 | 353.077   |  19.0013 |  83    |  8.3  |
| Okuwaki_et_al_2016        |    -71.741  |   -31.637  | 25      |   3.05545 |  15.0254 |  65.2  |  8.3  |
| SCARDEC                   |    -71.674  |   -31.573  | 17      |  12.3052  |  20.0012 | 110    |  8.3  |
| USGS                      |    -71.8928 |   -30.9101 | 15.05   | nan       | nan      |  83    |  8.3  |

### Rupture figure

![](earthquake_ruptures.png)

## References
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2015&mo=09&day=16&oyr=2015&omo=09&oday=16&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=8&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2022. 
- `earthquake_rupture_model_GFZ.xml`: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2015sfdd. Last accessed May 2022. 
- `earthquake_rupture_model_Hayes_2017.xml`, and `earthquake_rupture_model_Okuwaki_et_al_2016.xml`, `s2015ILLAPE01HAYE.fsp`, `s2015ILLAPE01OKUW.fsp`: Earthquake Source Model Database. http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s2015ILLAPE01HAYE/. Last accessed May 2022.
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20150917075433.html. Last accessed May 2022. 
- `earthquake_rupture_model_Matthew_Herman_et_al_2017.xml`: Downloaded from Matthew_Herman_et_al_2017: https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1002/2016JB013617. Herman, M. W., Nealy, J. L., Yeck, W. L., Barnhart, W. D., Hayes, G. P., Furlong, K. P., and Benz, H. M. (2017), Integrated geophysical characteristics of the 2015 Illapel, Chile, earthquake, J. Geophys. Res. Solid Earth, 122, 4691– 4711, doi:10.1002/2016JB013617. Last accessed May 2022. 
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/. Last accessed May 2022. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us20003k7a/atlas/1594162150247/download/rupture.json. Last accessed May 2022. 
- `CSN_Fase_w_4_OK.jpg`: PHASE W INVESTMENT USING CGPS ILLAPEL EARTHQUAKE. http://www.csn.uchile.cl/inversion-de-la-fase-w-usando-cgps/. Last accessed May 2022. 
- `Fase_w_2_CSN.jpg`: PHASE W EARTHQUAKE ILLAPEL 2015.https://www.csn.uchile.cl/fase-w-terremoto-illapel-2015/. Last accessed May 2022.
- `IPGP.jpg`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/seismes/events/2015/us20003k7a/carte.jpg. Last accessed May 2022.
- `IRIS.pdf`: Moment Tensor for MW 8.3 (GCMT) OFF COAST OF CENTRAL CHILE. http://ds.iris.edu/spud/momenttensor/11245859. Last accessed May 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2015&start_month=9&start_day=16&start_time=00%3A00%3A00&end_year=2015&end_month=9&end_day=17&end_time=00%3A00%3A00&min_dep=&max_dep=&min_mag=8&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed May 2022. Geophysical Survey of Russian Academy of Sciences (MOS) rupture model which has been exported from ISC.pdf. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_MOS.xml`. 