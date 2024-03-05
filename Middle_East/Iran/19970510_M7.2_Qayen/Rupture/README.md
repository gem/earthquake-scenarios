# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description    |
|:---------------------|:---------------|
| Fault mechanism       | Strike Slip    |
| Tectonic region type | Active Crustal |

### Preferred nodal plane solution

| source                         |   longitude |   latitude |   depth |   strike |      dip |   rake |   mag |
|:-------------------------------|------------:|-----------:|--------:|---------:|---------:|-------:|------:|
| Berberian_et_al_1999           |      59.81  |     33.84  |      13 |  155.904 |  89.0014 |   -160 |   7.2 |
| GCMT                           |      60.02  |     33.58  |      15 |  338.087 |  90      |   -173 |   7.2 |
| Sudhaus_And_Jonsson_et_al_2010 |      60.02  |     33.52  |       6 |  153.899 |  88.0009 |   -168 |   7.2 |
| USGS                           |      59.809 |     33.825 |      10 |  nan     | nan      |   -160 |   7.3 |
| Zarei_et_al_2019               |      59.81  |     33.88  |      13 |  155.904 |  88.9986 |   -160 |   7.2 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_GCMT.xml`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?itype=ymd&yr=1997&mo=5&day=10&oyr=1997&omo=5&oday=10&jyr=1976&jday=1&ojyr=1976&ojday=1&otype=nd&nday=1&lmw=7&umw=10&lms=0&ums=10&lmb=0&umb=10&llat=-90&ulat=90&llon=-180&ulon=180&lhd=0&uhd=1000&lts=-9999&uts=9999&lpe1=0&upe1=90&lpe2=0&upe2=90&list=0. Last accessed February 2023.
- `earthquake_rupture_model_Sudhaus_And_Jonsson_2012.xml`: Earthquake Source Model Database. http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1978TABASI01HART/. Rupture geometry from [SRCMOD - s1997ZIRKUH01SUDH.fsp](http://equake-rc.info/SRCMOD/searchmodels/viewmodel/s1997ZIRKUH01SUDH/). Last accessed February 2023.
- `earthquake_rupture_model_Sudhaus_And_Jonsson_et_al_2010.xml`: Henriette Sudhaus, Sigurjón Jónsson, Source model for the 1997 Zirkuh earthquake (MW = 7.2) in Iran derived from JERS and ERS InSAR observations, Geophysical Journal International, Volume 185, Issue 2, May 2011, Pages 676–692, https://doi.org/10.1111/j.1365-246X.2011.04973.x. Last accessed April 2022.
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp000820p/atlas/1594168408514/download/rupture.json. Last accessed February 2023.
- `earthquake_rupture_model_Walker_et_al_2011.xml`: R. T. Walker, E. A. Bergman, W. Szeliga, E. J. Fielding, Insights into the 1968-1997 Dasht-e-Bayaz and Zirkuh earthquake sequences, eastern Iran, from calibrated relocations, InSAR and high-resolution satellite imagery, Geophysical Journal International, Volume 187, Issue 3, December 2011, Pages 1577–1603, https://doi.org/10.1111/j.1365-246X.2011.05213.x. Last accessed November 2022.
- `earthquake_rupture_model_Zarei_et_al_2019.xml:` Zarei, S., Khatib, M.M., Zare, M. et al. Evaluation of Seismicity Triggering: Insights from the Coulomb Static Stress Changes after the 30 August 1968 Dasht-e-Bayaz Earthquake (Mw = 7.1), Eastern Iran. Geotecton. 53, 601–616 (2019). https://doi.org/10.1134/S0016852119050078. Last accessed November 2022. 
- `IRIS.pdf`: Moment Tensor for MW 7.2 (GCMT) NORTHERN AND CENTRAL IRAN. http://ds.iris.edu/spud/momenttensor/897520. Last accessed February 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?request=COMPREHENSIVE&out_format=FMCSV&bot_lat=&top_lat=&left_lon=&right_lon=&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg&searchshape=GLOBAL&srn=&grn=&start_year=1997&start_month=5&start_day=10&start_time=00%3A00%3A00&end_year=1997&end_month=5&end_day=10&end_time=23%3A59%3A00&min_dep=&max_dep=&min_mag=7&max_mag=&req_mag_type=&req_mag_agcy=&req_fm_agcy=Any&include_links=on. Last accessed February 2023.