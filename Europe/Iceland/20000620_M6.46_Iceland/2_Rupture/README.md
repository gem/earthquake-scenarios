# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Strike-slip          |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |     -20.76  |      63.98 |      10 |  279.247 | 90      |      0 |  6.46 |
| GCMT     |     -20.85  |      63.98 |      15 |  271.229 | 76.9993 |     -5 |  6.4  |
| USGS     |     -20.758 |      63.98 |      10 |  271.264 | 77.0024 |     -5 |  6.5  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp0009ux8/atlas/1594169845271/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR`: Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main

# Notes

- EFEHR's rupture file is generated from a source model that is got from the EFSM20 fault models database. These values were reviewed and it was concluded that the fault that was selected to represent the rupture of this earthquake, was not chosen correctly. The rupture that was chosen corresponds to a normal fault when the fault mechanism was strike-slip. Therefore, from the same database, the correct fault source mechanism was selected and the EFEHR rupture model was updated.