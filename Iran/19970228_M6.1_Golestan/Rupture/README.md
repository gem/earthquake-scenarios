# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Strike Slip    |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source             |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:-------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT               |       48.06 |     38.3   |      15 |  184.018 | 57.0029 |    -15 |   6.1 |
| Jackson_et_al_2002 |       47.79 |     38.1   |       9 |  183.007 | 81.0029 |     -1 |   6   |
| USGS               |       48.05 |     38.075 |      10 |  170.634 | 90      |    -15 |   6.1 |

### Rupture figure

![](earthquake_ruptures.png)


## References
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1997&mo=02&day=28&oyr=1976&omo=1&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023. 
- `earthquake_rupture_model_Jackson_et_al_2002.xml:` James Jackson, Keith Priestley, Mark Allen, Manuel Berberian, Active tectonics of the South Caspian Basin, Geophysical Journal International, Volume 148, Issue 2, February 2002, Pages 214–245, https://doi.org/10.1046/j.1365-246X.2002.01588.x. Last accessed May 2023.
- `earthquake_rupture_model_USGS.xml`: from `USGS.json` rupture. https://earthquake.usgs.gov/product/shakemap/usp0007y0b/atlas/1594168218770/download/rupture.json. Last accessed February 2023.