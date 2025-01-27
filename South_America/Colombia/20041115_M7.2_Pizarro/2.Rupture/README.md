# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Subduction Interface |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| GCMT     |    -77.57   |     4.72   |    16   |  20.985  |  10.9997 | 114    |   7.2 |
| ISC      |    -77.4512 |     4.6916 |    11.4 |  42.6205 |  33.0602 | 123.74 |   7.2 |
| RSNC     |    -77.79   |     4.81   |    10   |  21.9857 |  16      | 113    |   7.1 |
| USGS     |    -77.508  |     4.695  |    15   | nan      | nan      | 116    |   7.2 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2004&mo=11&day=15&oyr=2004&omo=11&oday=15&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed May 2022. 
- `earthquake_rupture_model_ISC.xml`: International Seismological Centre (ISC) On-Line Bulletin. http://isc-mirror.iris.washington.edu/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2004&start_month=11&start_day=15&start_time=00%3A00%3A00&end_year=2004&end_month=11&end_day=15&end_time=23%3A00%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed May 2022.
- `earthquake_rupture_model_RSNC.xml`: Localizacion Preliminar de Sismos Ubicados en le Territorio Colombiano. https://www2.sgc.gov.co/Publicaciones/Boletines%20Sismicidad/Bolet%C3%ADn%20Junio%20de%201994.pdf. Last accessed June 2023. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp000d8gx/atlas/1594172798367/download/rupture.json. Last accessed May 2022. 
- `IRIS.pdf`: Moment Tensor for MW 7.2 (GCMT) NEAR WEST COAST OF COLOMBIA. http://ds.iris.edu/spud/momenttensor/936890. Last accessed May 2022.
