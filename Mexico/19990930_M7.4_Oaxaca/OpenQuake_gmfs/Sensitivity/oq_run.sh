#!/bin/bash

oq engine --run job_rup-Hernandez_et_al_2001_gmpe-GEM_seismic.ini --log-file log_rup-Hernandez_et_al_2001_gmpe-GEM_seismic.txt
oq engine --run job_rup-Hernandez_et_al_2001_gmpe-USGS_seismic.ini --log-file log_rup-Hernandez_et_al_2001_gmpe-USGS_seismic.txt
oq engine --run job_rup-GCMT_gmpe-GEM_seismic.ini --log-file log_rup-GCMT_gmpe-GEM_seismic.txt
oq engine --run job_rup-GCMT_gmpe-USGS_seismic.ini --log-file log_rup-GCMT_gmpe-USGS_seismic.txt
oq engine --run job_rup-USGS_gmpe-GEM_seismic.ini --log-file log_rup-USGS_gmpe-GEM_seismic.txt
oq engine --run job_rup-USGS_gmpe-USGS_seismic.ini --log-file log_rup-USGS_gmpe-USGS_seismic.txt
