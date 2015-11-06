#!/usr/bin/python

'''
Prolog wrapper for docker images submission to batch systems

Created on Oct 28, 2015

@author: mariojmdavid@gmail.com
'''

import time
import os
import peUtils

if __name__ == '__main__':
    print '==========================================='
    ti = time.time()
    param = peUtils.getOptions()

    print 'I am the PROLOG of batch system'
    print '-------- The env variables --------'
    print os.environ
    print '-------- The config param ---------'
    print param
    print '-----------------------------------'
    bs = param['global']['batch_sys']
    comp_home = os.environ[param['global']['comp_home']]
    job_id = os.environ[param['global']['job_id']]
    comp_workdir = comp_home + os.sep + 'job_' + job_id

    '''
    try:
        os.makedirs(comp_workdir, 755)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e
        pass
    '''

    # The scp will have to be remodeled, for now just scp
    sub_host = os.environ[param['global']['sub_host']]
    sub_workdir = os.environ[param['global']['sub_workdir']]
    std_in = os.environ['SGEIN1']
    exec_job = os.environ[param['global']['job_script']]

    print '----------- Several things ----------'
    print 'Batch system: %s' % bs
    print 'Submit host: %s' % sub_host
    print 'Submit workdir: %s' % sub_workdir
    print 'Compute node workdir: %s' % comp_workdir
    print 'Exec script: %s' % exec_job
    print '-----------------------------------'

    os.system('scp -r -q %s:%s %s' % (sub_host, std_in, comp_workdir))
    os.system(exec_job)

    print '==========================================='
