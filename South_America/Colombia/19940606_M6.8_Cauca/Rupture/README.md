# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Strike-Slip          |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT     |     -75.94  |      2.93  |    15   |  206.004 | 76.0044 |   -170 |  6.8  |
| ISC      |     -76.057 |      2.917 |    12.1 |  214.005 | 86.9998 |   -169 |  6.76 |
| RSNC     |     -76.08  |      2.85  |    10   |  228.908 | 81.9998 |   -146 |  6.8  |
| USGS     |     -76.057 |      2.917 |    12.1 |  207.004 | 87.0008 |   -169 |  6.76 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1994&mo=6&day=6&oyr=1994&omo=6&oday=6&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6.5&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed July 2022. 
- `earthquake_rupture_model_ISC.xml`: International Seismological Centre (ISC) On-Line Bulletin. http://isc-mirror.iris.washington.edu/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=1994&start_month=6&start_day=06&start_time=00%3A00%3A00&end_year=1994&end_month=6&end_day=06&end_time=23%3A00%3A00&min_dep=&max_dep=&min_mag=6.5&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed July 2022.
- `earthquake_rupture_model_RSNC.xml`: Localizacion Preliminar de Sismos Ubicados en le Territorio Colombiano. https://www2.sgc.gov.co/Publicaciones/Boletines%20Sismicidad/Bolet%C3%ADn%20Junio%20de%201994.pdf. Last accessed June 2023. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0006dv8/atlas/1594167275768/download/rupture.json. Last accessed July 2022.
- `IRIS.pdf`: Moment Tensor for MW 6.8 (GCMT) COLOMBIA. http://ds.iris.edu/spud/momenttensor/884475. Last accessed July 2022.
