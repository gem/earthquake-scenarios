import os, sys
import copy
from openquake.commonlib import readinput, logs
from openquake.engine.engine import create_jobs, run_jobs


def main(job_ini, rup_files, gmlt_files, max_distances=None, 
         concurrent_jobs=1, out_folder='Sensitivity'):
    '''
    Funtion to run sensitivity analysis for ruptures and gmlt.

    Parameters
    ----------
    job_ini : str
        Path to OQ job.ini file to be used as a reference.

    rup_files : list of strings
        List of rupture file paths (path relative to OQ job.ini)

    gmlt_files : list of strings
        List of gmlt file paths (path relative to OQ job.ini)

    max_distances: list of floats
        Maximum distance (from the rupture) to consider stations data.

    concurrent_jobs : int
        Number of concurrent jobs to run

    out_folder : str
        Folder name to save log files (it will be relative to the location of the job.ini)
    
    Returns
    -------
    Runs OpenQuake calculations and save log files in a `Sensitivty` folder
    '''
    
    # Get job parameters
    params = readinput.get_params(job_ini)
    base_path = params['base_path']

    # Build one dictionary of parameters for each rupture model
    allparams = []
    for gmlt in gmlt_files:
        gmpe_name = gmlt[16:-4]
        for rupture in rup_files:
            rup_name = rupture[36:-4]
            if max_distances:
                for max_dist in max_distances:
                    par = copy.deepcopy(params)
                    par['description'] = par['description'] + f', gmlt:{gmpe_name}' + f', Rupture:{rup_name}' + f', Max_dist:{max_dist}km'
                    par['inputs']['rupture_model'] = os.path.join(base_path, rupture)
                    par['inputs']['gsim_logic_tree'] = os.path.join(base_path, gmlt)
                    par['maximum_distance_stations'] = f'{max_dist}'
                    allparams.append(par)
            else:
                par = copy.deepcopy(params)
                par['description'] = par['description'] + f', gmlt:{gmpe_name}' + f', Rupture:{rup_name}'
                par['inputs']['rupture_model'] = os.path.join(base_path, rupture)
                par['inputs']['gsim_logic_tree'] = os.path.join(base_path, gmlt)
                allparams.append(par)                

    # Build a job for each rupture model
    jobs = create_jobs(allparams, multi=True)  # independent jobs

    # Run the jobs (possibility for parallel calcs)
    run_jobs(jobs, concurrent_jobs) # concurrent_jobs=1

    # Save the logs
    for job in jobs:
        save_log = os.path.join(base_path, out_folder, f'log_calc_{job.calc_id}.txt')
        rows = logs.dbcmd(
            'SELECT job_id, message FROM log WHERE job_id=?x', job.calc_id)       
        with open(save_log, 'w') as f:
            f.write(f'job_id: {job.calc_id}\n')
            f.write(f'''job_description: {job.params['description']}\n\n''')
            for row in rows:
                f.write(row.message + '\n')
        f.close()
    
    return jobs

if __name__ == '__main__':
    job = sys.argv[1]
    rup_files = sys.argv[2]
    gmlt_files = sys.argv[3]

    main(job, rup_files, gmlt_files)
