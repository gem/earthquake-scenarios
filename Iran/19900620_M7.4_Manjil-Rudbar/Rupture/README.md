# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Strike slip    |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source               |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:---------------------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| Berberian_et_al_1992 |      49.41  |     36.96  |    14   |  292.282 |  87.9963 |     -9 |   7.3 |
| GCMT                 |      49.52  |     36.95  |    15   |  300.295 |  72.9995 |     32 |   7.4 |
| Gao_And_Wallace_1994 |      49.34  |     36.96  |    14   |  288.251 |  88.0009 |     -4 |   7.2 |
| USGS                 |      49.409 |     36.957 |    18.5 |  nan     | nan      |     -9 |   7.4 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_Berberian_et_al_1992.xml`: M. Berberian, M. Qorashi, J. A. Jackson, K. Priestley, T. Wallace; The Rudbar-Tarom earthquake of 20 June 1990 in NW Persia: Preliminary field and seismological observations, and its tectonic significance. Bulletin of the Seismological Society of America 1992; 82 (4): 1726–1755. doi: https://doi.org/10.1785/BSSA0820041726. Last accessed November 2022.
- `earthquake_rupture_model_Gao_And_Wallace_1994.xml`: Gao, L., & Wallace, T. C. (1994). Aftershocks of the 1990 western Iran (MW 7.3) earthquake. Bull. seism. Soc. Am. Last accessed February 2023.
- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1990&mo=6&day=20&oyr=1990&omo=6&oday=20&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023. 
- `earthquake_rupture_model_USGS.xml`: from `USGS.json` rupture. https://earthquake.usgs.gov/product/shakemap/usp0004arq/atlas/1594166331706/download/rupture.json. Last accessed February 2023.
- `IRIS.pdf`: Moment Tensor for MW 7.4 (GCMT) Western Iran. http://ds.iris.edu/spud/momenttensor/869970. Last accessed February 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?event_id=366754&out_format=ISF2&request=COMPREHENSIVE. Last accessed February 2023.