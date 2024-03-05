# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse Fault        |
| Tectonic region type | Subduction Interface |

### Preferred nodal plane solution

| source                       |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:-----------------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT                         |     -84.58  |      9.45  |    29.6 |  294.014 | 23.9997 |     86 |   6.6 |
| GFZ                          |     -84.47  |      9.63  |    25   |  291.015 | 20.0004 |     79 |   6.6 |
| IPGP                         |     -84.505 |      9.526 |    20   |  302.012 | 22.0005 |     93 |   6.6 |
| Quintero_Quintero_et_al_2021 |     -84.546 |      9.463 |    27   |  289.009 | 17.0009 |     85 |   6.4 |
| USGS                         |     -84.487 |      9.515 |    19.4 |  316.005 | 28.0015 |    123 |   6.5 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2017&mo=11&day=13&oyr=2017&omo=11&oday=13&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6.3&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed August 2022.
- `earthquake_rupture_model_GFZ.xml`: http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2017wfnw. Last accessed August 2022. 
- `earthquake_rupture_model_IPGP.xml`: The automatic real-time STFs since 2014. http://geoscope.ipgp.fr/index.php/en/catalog/earthquake-description?seis=us2000bmhe. Last accessed August 2022.
- `earthquake_rupture_model_Quintero_Quintero_et_al.xml`: Quintero-Quintero, R., Campos-Durán, D., Porras-Espinoza, H., Segura-Torres, J., 2021, Análisis de sismos interplaca, Pacifíco central de Costa Rica: los sismos de Esterillos (13 de noviembre de 2017) y Herradura (24 de agosto de 2020): Boletín de la Sociedad Geológica Mexicana, 73 (2), A100121. http://dx.doi.org/10.18268/BSGM2021v73n2a100121. Last accessed August 2022.
- `earthquake_rupture_model_SCARDEC.xml`: A new database of Source Time Functions (STFs) extracted from the SCARDEC method. STFs provided here have been revised and are therefore provided with a delay. http://scardec.projects.sismo.ipgp.fr/#. Last accessed August 2022.
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us2000bmhe/atlas/1594400127475/download/rupture.json. Last accessed August 2022. 
- `IRIS.pdf`: Moment Tensor for MW 6.6 (GCMT) COSTA RICA. http://ds.iris.edu/spud/momenttensor/16387167. Last accessed August 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://isc-mirror.iris.washington.edu/cgi-bin/web-db-run?event_id=616640579&out_format=ISF2&request=COMPREHENSIVE. Last accessed August 2022. 