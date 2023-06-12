# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source        |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:--------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR         |     15.95   |    45.85   |    10   |  51.9822 | 64.9968 |     35 |   5.1 |
| GCMT          |     16.07   |    45.79   |    12   |  56.9713 | 49.9982 |     66 |   5.4 |
| GEOFON        |     15.99   |    45.88   |    10   |  73.9723 | 39.9991 |     86 |   5.3 |
| Heraketal2021 |     16.028  |    45.879  |    10.1 |  66.9724 | 47.0011 |     79 |   5.4 |
| USGS          |     15.9697 |    45.9072 |    10   |  73.9781 | 51.0074 |     84 |   5.1 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us70008dx7/atlas/1646888990989/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR`: Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main
- '[Herak_et_al_2021.pdf]`: Markušić, Snježana & Stanko, Davor & Korbar, Tvrtko & Belić, Nikola & Penava, Davorin & Kordic, Branko. (2020). The Zagreb (Croatia) M5.5 Earthquake on 22 March 2020. Geosciences. 10. 252. 10.3390/geosciences10070252. You can see this document in this folder. Last accessed May 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Heraketal2021.xml`.
- 'GEOFON': Source mechanism obtained from http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2020fskl
