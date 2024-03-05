# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Strike-slip          |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |     -21.01  |     64     |      10 |  279.203 | 90      |      0 |  6.32 |
| GCMT     |     -21.17  |     63.92  |      12 |  267.2   | 78.0024 |     -7 |  6.3  |
| USGS     |     -21.013 |     64.005 |       9 |  267.2   | 78.0023 |     -7 |  6.3  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp000g826/atlas/1600702418243/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR`: Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main

# Notes

- EFEHR's rupture file is generated from a source model that is got from the EFSM20 fault models database. These values were reviewed and it was concluded that the fault that was selected to represent the rupture of this earthquake, was not chosen correctly. The rupture that was chosen corresponds to a normal fault when the fault mechanism was strike-slip. Therefore, from the same database, the correct fault source mechanism was selected and the EFEHR rupture model was updated.