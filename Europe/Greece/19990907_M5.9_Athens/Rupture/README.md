# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal               |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |      23.58  |     38.08  |    16.8 |  162.965 | 43.941  |    -90 |   5.9 |
| ESM      |      23.582 |     38.122 |     9.4 |  114.966 | 57.0002 |    -80 |   5.9 |
| GCMT     |      23.64  |     37.87  |    15   |  115.969 | 38.9995 |    -81 |   6   |
| USGS     |      23.605 |     38.119 |    10   |  123.037 | 63.3145 |    -81 |   6   |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0009e46/atlas/1594169354546/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR` - Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main
- `ESM.PDF` - Rupture obtained from https://esm-db.eu/#/event/GR-1999-0001

# Notes

- The rupture geometry in `xml` defined by EFEHR generates a strike in OpenQuake of 342.99 (despite indicating in the `xml` a value of 113). Therefore the order of the right and left coordinates was modified, generating now in OQ a strike value of 162.965.
