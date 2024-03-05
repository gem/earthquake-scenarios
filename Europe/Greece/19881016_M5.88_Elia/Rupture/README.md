# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Strike-slip          |
| Tectonic region type | Subduction Interface |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |      20.9   |     37.95  |    29   |  300.02  | 30.0025 |     90 |  5.88 |
| GCMT     |      20.9   |     37.95  |    29   |  301.029 | 76.0038 |     -3 |  5.8  |
| USGS     |      20.932 |     37.938 |    25.2 |  301.035 | 76.0002 |     -3 |  5.9  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0003mvg/atlas/1594165928190/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR` - Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main

## Notes

- EFEHR's rake value suggests that the fault mechanism was reverse, and even though the other sources say the rupture was strike-slip since the region is located in the Hellenic Arc-Trench System (subduction zone), this value was mantained.