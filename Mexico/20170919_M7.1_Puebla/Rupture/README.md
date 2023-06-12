# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal               |
| Tectonic region type | Subduction Intraslab |

### Preferred nodal plane solution

| source            |   longitude |   latitude |   depth |   strike |   dip |   rake |   mag |
|:------------------|------------:|-----------:|--------:|---------:|------:|-------:|------:|
| GCMT              |    -98.63   |    18.59   |    51   |   108.94 | 46    |    -97 |   7.1 |
| GFZ               |    -98.49   |    18.56   |    50   |   103.94 | 49    |    -98 |   7.1 |
| IPGP              |    -98.399  |    18.584  |    58   |   110.94 | 37    |    -91 |   7.1 |
| JMA               |    -98.255  |    18.354  |    50   |   108.94 | 45    |    -96 |   7.1 |
| Melgar_et_al_2018 |    -98.6878 |    18.3044 |    57.5 |   119.04 | 43.91 |    -82 |   7.1 |
| SSN               |    -98.6712 |    18.3297 |    51.2 |   111.94 | 46    |    -93 |   7.1 |
| USGS              |    -98.4887 |    18.5499 |    48   |   109.35 | 45.82 |    -93 |   7.1 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2017&mo=09&day=19&oyr=1976&omo=&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=0&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=48&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed April 2022.
- `earthquake_rupture_model_GFZ.xml`: available at http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2017skgl. Last accessed April 2022.
- `earthquake_rupture_model_IPGP.xml`: The automatic real-time STFs since 2014. http://www.ipgp.fr/fr/observatoires-volcanologiques-sismologiques. Last accessed April 2022.
- `earthquake_rupture_model_JMA.xml`: Japan Meteorological Agency (JMA). https://www.data.jma.go.jp/svd/eqev/data/mech/world_cmt/fig/cmt20170919181439.html. Last accessed April 2022. 
- `earthquake_rupture_model_Melgar_et_al_2018_xml`: Bend Faulting at the Edge of a Flat Slab: The 2017 Mw7.1 Puebla-Morelos, Mexico Earthquake. Geophysical Research Letters, 45, 2633– 2641. https://doi.org/10.1002/2017GL076895. Last accessed Oct 2022.
- `earthquake_rupture_model_SSN.xml`: Report from the Servicio Sismológico Nacional (SSN, National Geological Survey) `SSNMX_rep_esp_20170919_Puebla-Morelos.pdf`. http://www.ssn.unam.mx/sismicidad/reportes-especiales/. Last accessed April 2022.
- `earthquake_rupture_model_USGS.xml`: USGS.json rupture. https://earthquake.usgs.gov/product/shakemap/us2000ar20/atlas/1594399976203/download/rupture.json. Last accessed April 2022.
- `IRIS.pdf`: Moment Tensor. Reference from GCMT. http://ds.iris.edu/spud/momenttensor/17998511. Last accessed April 2022.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2017&start_month=9&start_day=19&start_time=00%3A00%3A00&end_year=2017&end_month=9&end_day=19&end_time=23%3A59%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed April 2022. 