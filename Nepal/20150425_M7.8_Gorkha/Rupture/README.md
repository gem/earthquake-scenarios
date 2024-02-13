# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism      | Thrust/reverse       |
| Tectonic region type | Subduction interface |

### Preferred nodal plane solution

| source    |   longitude |   latitude |   depth | strike   | dip   |   rake |   mag |
|:----------|------------:|-----------:|--------:|:---------|:------|-------:|------:|
| Hayes     |     84.65   |    28.13   |    15   |          |       | 102.13 |  7.82 |
| Kobayashi |     84.7079 |    28.1473 |    15   |          |       |  98.37 |  7.84 |
| Stevens   |     84.708  |    28.147  |    12   |          |       |  90    |  7.8  |
| USGS      |     84.7314 |    28.2305 |     8.2 |          |       | 102.13 |  7.8  |
| Yagi      |     84.708  |    28.147  |    15   |          |       |  89.29 |  7.9  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `ESMD_Hayes.pdf`: Hayes GP, Briggs RW, Barnhart WD, Yeck WL, McNamara DE, Wald DJ, Nealy JL, Benz HM, Gold RD, Jaiswal KS,  Marano K, Earle PS, Hearne MG, Smoczyk GM, Wald LA, Samsonov SV (2015). Rapid characterization of the 2015 Mw 7.8 Gorkha, Nepal, earthquake sequence and its seismotectonic context. Seismological Research Letters, 86(6):1557-1567. https://doi.org/10.1785/0220150145. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Hayes.xml`.

- `ESMD_Kobayashi.pdf`: Kobayashi T, Morishita Y, Yarai H (2015). Detailed crustal deformation and fault rupture of the 2015 Gorkha earthquake, Nepal, revealed from ScanSAR-based interferograms of ALOS-2. Earth, Planets and Space, 67(1):1-13. https://doi.org/10.1186/s40623-015-0359-z. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Kobayashi.xml`.

- `ESMD_Yagi.pdf`: Yagi Y, Okuwaki R (2015). Integrated seismic source model of the 2015 Gorkha, Nepal, earthquake. Geophysical Research Letters, 42(15):6229-6235. https://doi.org/10.1002/2015GL064995. Available online at: http://equake-rc.info/SRCMOD/searchmodels/listevents/. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Yagi.xml`.

- `Stevens_et_al.pdf`: Stevens V, Shrestha S, Maharjan D (2018). Probabilistic Seismic Hazard Assessment of Nepal. Bulletin of the Seismological Society of America 2018; 108 (6): 3488–3510. https://doi.org/10.1785/0120180022. Last accessed August 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_Stevens.xml`.
  
- `USGS.json`: USGS rupture. Available online at: https://earthquake.usgs.gov/product/shakemap/us20002926/atlas/1594162031303/download/rupture.json. Last accessed March 2023. Earthquake rupture model input file in the OQ format saved as `earthquake_rupture_model_USGS.xml`.
