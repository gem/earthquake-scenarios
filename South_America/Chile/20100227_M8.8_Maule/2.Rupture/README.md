# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description   |
|:---------------------|:--------------|
| Fault mechanism       | Reverse       |
| Tectonic region type | Subduction    |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth | strike   | dip   |   rake |   mag |
|:---------|------------:|-----------:|--------:|:---------|:------|-------:|------:|
| GCMT     |     -73.15  |   -35.98   |    23.2 | 19.84    | 18.0  |    116 |   8.8 |
| IRIS     |     -73.15  |   -35.98   |    23.2 | 19.84    | 18.0  |    116 |   8.8 |
| ISC      |     -73.15  |   -35.98   |    23.2 | 19.84    | 18.0  |    116 |   8.8 |
| JMA      |     -72.59  |   -36.0267 |    20   | 12.66    | 12.0  |    105 |   8.8 |
| SCARDEC  |     -72.9   |   -36.12   |    24   | 24.96    | 18.0  |    117 |   8.8 |
| USGS     |     -72.898 |   -36.122  |    22.9 |          |       |    116 |   8.8 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2010&mo=2&day=27&oyr=2010&omo=2&oday=27&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=8&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed August 2022. 
- `earthquake_rupture_model_IRIS.xml`: Moment Tensor for MW 8.8 (GCMT) OFF COAST OF CENTRAL CHILE. http://ds.iris.edu/spud/momenttensor/987510. Last accessed August 2022.
- `earthquake_rupture_model_ISC.xml`: International Seismological Centre (ISC) On-Line Bulletin. www.isc.ac.uk/cgi-bin/web-db-run?event_id=14340585&out_format=ISF2&request=COMPREHENSIVE. Last accessed August 2022. Geophysical Survey of Russian Academy of Sciences (MOS) rupture model which has been exported from ISC.pdf. 
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20100227153414.html. Last accessed August 2022. 
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/. Last accessed August 2022. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/official20100227063411530_30/atlas/1594161725779/download/rupture.json. Last accessed August 2022. 
- `FFM.geojson`: USGS Finite Fault Model. https://earthquake.usgs.gov/earthquakes/eventpage/official20100227063411530_30/finite-fault. Last accessed August 2022.
- `GFZ.txt` and `GFZ.pdf` downloaded from: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2010eaoy. Last accessed August 2022. 
- `IPGP.jpg`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/seismes/events/2010/chil10058/event.html. Last accessed August 2022.
- `SRCMOD`: Earthquake Source Model Database. http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed August 2022. 