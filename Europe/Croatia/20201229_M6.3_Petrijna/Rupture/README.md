# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Reverse              |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |     16.22   |    45.42   |    10   |  325.049 | 61.9982 |    145 |   6.3 |
| GCMT     |     16.22   |    45.36   |    12   |  131.921 | 78.9997 |    170 |   6.4 |
| GEOFON   |     16.21   |    45.48   |    10   |  129.916 | 82.0001 |    177 |   6.4 |
| INGV     |     16.202  |    45.403  |     9.1 |  127.923 | 89.0007 |   -179 |   6.3 |
| USGS     |     16.2573 |    45.4244 |    10   |  130.767 | 83.3266 |    179 |   6.3 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us6000d3zh/atlas/1646891567521/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR`: Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main
- `INGV`: Rupture obtained from http://terremoti.ingv.it/en/event/25870121#MeccanismoFocale. Last accessed May 2023.
- `GEOFON`: Rupture obtained from http://geofon.gfz-potsdam.de/eqinfo/event.php?id=gfz2020zocb. Last accessed May 2023.

## Notes

- The rupture geometry in `xml` defined by USGS generates a strike in OpenQuake of 310.835 (despite indicating in the `xml` a value of 134). Therefore the order of the right and left coordinates was modified, generating now in OQ a strike value of 130.767.