# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description        |
|:---------------------|:-------------------|
| Fault mechanism       | Normal             |
| Tectonic region type | Stable Continental |

### Preferred nodal plane solution

| source             |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:-------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| Ahorneretal1994    |       5.952 |     51.17  |   14.6  |  123.979 | 67.9955 | -90    |   5.3 |
| Camelbeecketal1994 |       5.953 |     51.163 |   17.4  |  126.976 | 69.9971 | -90    |   5.4 |
| EFEHR              |       5.93  |     51.17  |   15    |  137.992 | 58.0031 | -98    |   5.3 |
| GCMT               |       5.63  |     51.56  |   15    |  142.988 | 68.0006 | -87    |   5.3 |
| ISC                |       5.78  |     51.19  |   19.68 |  130.249 | 66.7059 | -89.98 |   5.3 |
| USGS               |       5.798 |     51.153 |   21.2  |  147.952 | 16.2875 | -87    |   5.3 |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp00055q3/atlas/1594166749315/download/rupture.json. Last accessed January 2023.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR`: Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main

## Notes

- Rake angle is referenced as 82 deg (EFEHR), when the source, Baunmiller et al 1993, wrote it was 262º. Therefore, the real angle should be -98 deg. Also, because the fault according to the author is said to be almost pure normal. Therefore, the angle was modified in the xml file.