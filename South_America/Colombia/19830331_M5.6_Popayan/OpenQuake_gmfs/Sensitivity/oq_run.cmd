oq engine --run job_rup-GCMT_gmpe-GEM_all.ini
oq engine --sl -1 > log_rup-GCMT_gmpe-GEM_all.txt
oq engine --run job_rup-GCMT_gmpe-USGS_all.ini
oq engine --sl -1 > log_rup-GCMT_gmpe-USGS_all.txt
oq engine --run job_rup-USGS_gmpe-GEM_all.ini
oq engine --sl -1 > log_rup-USGS_gmpe-GEM_all.txt
oq engine --run job_rup-USGS_gmpe-USGS_all.ini
oq engine --sl -1 > log_rup-USGS_gmpe-USGS_all.txt
