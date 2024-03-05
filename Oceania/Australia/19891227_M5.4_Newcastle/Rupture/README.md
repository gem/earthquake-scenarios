# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description                       |
|:---------------------|:----------------------------------|
| Fault mechanism       | Thrust/reverse                    |
| Tectonic region type | Stable Continental Regions (SCRs) |

### Preferred nodal plane solution

| source                    |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:--------------------------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| AUS                       |     151.61  |    -32.95  |    11.5 |  104.012 | 31.9991 |     35 | 5.438 |
| Jackson_And_McKenzie_2022 |     151.61  |    -32.93  |    11   |  134.997 | 45.0074 |     90 | 5.2   |
| USGS                      |     151.619 |    -32.967 |    10   |  134.998 | 44.9979 |     90 | 5.4   |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `earthquake_rupture_model_AUS.xml`: Australian earthquake fault plane solutions. https://d28rz98at9flks.cloudfront.net/37302/Rec2002_019.pdf. Last accessed May 2023.
- `earthquake_rupture_model_Jackson_And_McKenzie_2022.xml`: Jackson, J., & McKenzie, D. (2022). The exfoliation of cratonic Australia in earthquakes. Earth and Planetary Science Letters, 578, 117305. https://doi.org/10.1016/j.epsl.2021.117305. Last accessed May 2023.  
- `earthquake_rupture_model_USGS.xml`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/usp00043na/atlas/1594166135203/download/rupture.json. Last accessed May 2023.
- `ISC.pdf`: International Seismological Centre (ISC) On-Line Bulletin. http://www.isc.ac.uk/cgi-bin/web-db-run?event_id=385153&out_format=ISF2&request=COMPREHENSIVE. Last accessed May 2023.


# Notes

- The fault plane solution from `AUS` indicated a magnitude `mb=5.7, ML=5.6`. The conversion equation from `Gaull et al., 1990`[^1] to estimate Mw was used (`Mw = 0.78ML + 1.07`), which considers a standard error of 0.27 magnitude units.

[^1]: Gaull et al., 1990, Are Australian earthquakes different?: Bulletin of the Seismological Society of America, v. 80, no. 4, p. 776-809.