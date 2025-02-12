# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal               |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |      22.176 |    37.014  |     6   |   19.971 | 45.0024 |    -90 |   6   |
| ESM      |      22.14  |    37.1167 |     8   |  201.033 | 45.0025 |    -77 |   5.9 |
| GCMT     |      22.64  |    36.8    |    15   |  221.042 | 55.9963 |    -56 |   5.9 |
| USGS     |      22.175 |    37.014  |    11.2 |  220.041 | 57.0015 |    -56 |   6   |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0002y1v/atlas/1594165613789/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR` - Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main
- `ESM.PDF` - Rupture obtained from https://esm-db.eu/#/event/GR-1986-0006

## Notes

-  EFEHR's rupture model had a rake of 90 degrees got from Gariel et al. (1991). However, since the same document expresses that the fault mechanism is normal, this value was change from 90 to -90 degrees.