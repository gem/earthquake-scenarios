
# SENSITIVITY ANALYSIS

This folder includes the following information:

### `oq_calcs_summary.csv`
Details on the calculations carried out in the sensitivity analysis.

It includes information for:
- `calc_id`: unique identifier for the calculation.
- `description`: details on the calculation
- `cal_time`: time of the calculation.
- `gmpe`: Ground Motion Prediction Equation (ground motion model).
- `imt`: Intensity measure type.
- `nominal_bias`: 
- `max_gmv`: Maximum ground motion value.
- `Rupture`: Rupture model used in the calculation.
- `GMLT`: Ground Motion Logic Tree used in the calculation.
- `Recording_Stations`: "All" stations (seismic + macroseismic), or only "seismic" stations.


### `job_rup-XXX_gmpe-YYY_ZZZ.ini`
Configuration file for running OpenQuake calculations.
It makes reference to a given rupture model (`rup-XXX`), a GMPE (`gmpe-YYY`) and the recording stations (`ZZZ`).

### `log_rup-XXX_gmpe-YYY_ZZZ.txt`
File with the OpenQuake running information in a _.txt_ format. This file includes the `nominal bias` estimates per GMPE.
It makes reference to a given rupture model (`rup-XXX`), a GMPE (`gmpe-YYY`) and the recording stations (`ZZZ`).

