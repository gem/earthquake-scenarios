# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description           |
|:---------------------|:----------------------|
| Fault mechanism       | Reverse               |
| Tectonic region type | Subduction Intrerface |

### Preferred nodal plane solution

| source             |   longitude |   latitude |   depth |   strike |       dip |    rake |   mag |
|:-------------------|------------:|-----------:|--------:|---------:|----------:|--------:|------:|
| ESMD               |    -102.57  |      18.18 |    17   |  300.135 |  13.9845  | 61.3056 |  8.01 |
| Eissler_et_al_1986 |    -102.31  |      18.72 |    17   |  288.215 |   9.00029 | 72      |  8    |
| GCMT               |    -101.99  |      17.91 |    21.3 |  301.169 |  18.0004  | 85      |  8    |
| USGS               |    -102.533 |      18.19 |    27.9 |  nan     | nan       | 85      |  8    |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_Eissler_et_al_1986.xml`: The focal mechanism for Michoacán_1985. Eissler, H., Astiz, L., & Kanamori, H. (1986). Tectonic setting and source parameters of the September 19, 1985 Michoacan, Mexico earthquake. Geophysical Research Letters, 13(6), 569-572. https://doi.org/10.1029/GL013i006p00569. Last accessed June 2022. 
- `earthquake_rupture_model_ESMD.xml`: Downloaded from Earthquake Source Model Database(ESMD). http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1985MICHOA01MEND/. Last accessed June 2022. 
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1985&mo=09&day=19&oyr=1985&omo=09&oday=19&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed June 2022. 
- `earthquake_rupture_model_USGS.xml`: USGS ruptures. https://earthquake.usgs.gov/product/shakemap/usp0002jwe/atlas/1594165429053/download/rupture.json. Last accessed June 2022.
- `IRIS.pdf`: Moment Tensor for MW 8.0 (GCMT) NEAR COAST OF GUERRERO, MEXICO. http://ds.iris.edu/spud/momenttensor/851735. Last accessed June 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?event_id=516095&out_format=ISF2&request=COMPREHENSIVE. Last accessed June 2022. 