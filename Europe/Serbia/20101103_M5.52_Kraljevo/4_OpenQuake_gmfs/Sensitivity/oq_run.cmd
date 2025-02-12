oq engine --run job_rup-EFEHR_gmpe-USGS_all.ini
oq engine --sl -1 > log_rup-EFEHR_gmpe-USGS_all.txt
oq engine --run job_rup-USGS_gmpe-USGS_all.ini
oq engine --sl -1 > log_rup-USGS_gmpe-USGS_all.txt
oq engine --run job_rup-EFEHR_gmpe-GEM_all.ini
oq engine --sl -1 > log_rup-EFEHR_gmpe-GEM_all.txt
oq engine --run job_rup-USGS_gmpe-GEM_all.ini
oq engine --sl -1 > log_rup-USGS_gmpe-GEM_all.txt
