# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Strike-slip          |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |       20.6  |      38.67 |      11 |  23.9526 | 79.9994 |    170 |   6.5 |
| GCMT     |       20.53 |      38.47 |      15 |  21.9469 | 63.9983 |    179 |   6.5 |
| USGS     |       20.6  |      38.67 |      11 |  24.5081 | 64.3878 |    155 |   6.5 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us10003ywp/atlas/1594161841609/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR` - Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main

# Notes

- The rupture geometry in `xml` defined by USGS generates a strike in OpenQuake of 204.692 (despite indicating in the `xml` a value of 21). Therefore the order of the right and left coordinates was modified, generating now in OQ a strike value of 20.5081.