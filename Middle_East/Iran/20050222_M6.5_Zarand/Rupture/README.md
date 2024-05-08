# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Thrust         |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source              |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:--------------------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| GCMT                |      56.81  |     30.76  |      12 |  266.052 |  47.0011 |    100 |   6.4 |
| Nicknam_et_al_2010  |      56.84  |     30.74  |      11 |  269.054 |  48.9979 |    114 |   6.4 |
| Talebian_et_al_2006 |      56.736 |     30.774 |       7 |  270.052 |  59.9996 |    104 |   6.4 |
| USGS                |      56.816 |     30.754 |      14 |  nan     | nan      |    104 |   6.4 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=2005&mo=2&day=22&oyr=1976&omo=1&oday=1&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=6&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023. 
- `earthquake_rupture_model_Nicknam_et_al_2010`:  Ahmad Nicknam, Reza Abbasnia, Mohsen Bozorgnasab & Yasser Eslamian (2010) Synthesizing Strong Motion Using Empirical Green's Function and Genetic Algorithm Approach, Journal of Earthquake Engineering, 14:4, 512-526, DOI: 10.1080/13632460903387103. Last accessed April 2022. 
- `earthquake_rupture_model_Talebian_et_al_2006`: M. Talebian, J. Biggs, M. Bolourchi, A. Copley, A. Ghassemi, M. Ghorashi, J. Hollingsworth, J. Jackson, E. Nissen, B. Oveisi, B. Parsons, K. Priestley, A. Saiidi, The Dahuiyeh (Zarand) earthquake of 2005 February 22 in central Iran: reactivation of an intramountain reverse fault, Geophysical Journal International, Volume 164, Issue 1, January 2006, Pages 137–148, https://doi.org/10.1111/j.1365-246X.2005.02839.x. Last accessed April 2022. 
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp000dgpx/atlas/1594173046564/download/rupture.json. Last accessed February 2023.
- `IRIS.xml`: Moment Tensor for MW 6.4 (GCMT) NORTHERN AND CENTRAL IRAN. http://ds.iris.edu/spud/momenttensor/940735. Last accessed February 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=2005&start_month=2&start_day=22&start_time=00%3A00%3A00&end_year=2005&end_month=2&end_day=22&end_time=23%3A00%3A00&min_dep=&max_dep=&min_mag=6.2&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed February 2023.