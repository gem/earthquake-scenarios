# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Thrust         |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source                    |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:--------------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| GCMT                      |      57.02  |     33.37  |    11   |  328.051 | 33.0004 |    107 |  7.3  |
| Hartzell_And_Mendoza_1991 |      57.36  |     33.22  |     5.5 |  330.184 | 24.9633 |    125 |  7.09 |
| Niazi_And_Kanamori_1981   |      57.434 |     33.386 |    33   |  330.05  | 30.0003 |    110 |  7.4  |
| Vahidifard_et_al_2017     |      57.34  |     33.145 |    42   |  330.047 | 25.0005 |    125 |  7.4  |
| Walker_et_al_2003         |      57.38  |     33.24  |     9   |  354.977 | 15.9998 |    155 |  7.28 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1978&mo=9&day=16&otype=ymd&oyr=1978&omo=10&oday=16&jyr=1976&jday=1&ojyr=1976&ojday=1&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023.
- `earthquake_rupture_model_Hartzell_And_Mendoza_1991.xml`: Earthquake Source Model Database. http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1978TABASI01HART/. Rupture geometry from [SRCMOD - s1978TABASI01HART.fsp](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1978TABASI01HART/). Last accessed February 2023.
- `earthquake_rupture_model_Niazi_And_Kanamori_1981.xml`: Niazi, M., & Kanamori, H. (1981). Source parameters of 1978 Tabas and 1979 Qainat, Iran, earthquakes from long-period surface waves. Bulletin of the Seismological Society of America, 71(4), 1201-1213. https://doi.org/10.1785/BSSA0710041201. Last accessed November 2022.
- `earthquake_rupture_model_Vahidifard_et_al_2017.xml`: Vahidifard, H., Zafarani, H. & Sabbagh-Yazdi, S.R. Hybrid broadband simulation of strong-motion records from September 16, 1978, Tabas, Iran, earthquake (M w 7.4). Nat Hazards 87, 57–81 (2017). https://doi.org/10.1007/s11069-017-2753-2. Last accessed April 2023.
- `earthquake_rupture_model_Walker_et_al_2003.xml`: Richard Walker, James Jackson, Calum Baker, Surface expression of thrust faulting in eastern Iran: source parameters and surface deformation of the 1978 Tabas and 1968 Ferdows earthquake sequences, Geophysical Journal International, Volume 152, Issue 3, March 2003, Pages 749–765, https://doi.org/10.1046/j.1365-246X.2003.01886.x. Last accessed February 2023.
- `IRIS.pdf`: Moment Tensor. Reference from GCMT.http://ds.iris.edu/spud/momenttensor/830735. Last accessed February 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&searchshape=RECT&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&srn=&grn=&start_year=1978&start_month=9&start_day=16&start_time=00%3A00%3A00&end_year=1978&end_month=9&end_day=16&end_time=23%3A59%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=MW&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed February 2023.
- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0000wjx/atlas/1594164041479/download/rupture.json. Last accessed February 2023.