#!/usr/bin/python

'''
Epilog wrapper for docker images submission to batch systems

Created on Oct 28, 2015

@author: mariojmdavid@gmail.com
'''

import time
import os
import peUtils


if __name__ == '__main__':
    print '==========================================='
    print '==========================================='
    ti = time.time()
    print 'I am the EPILOG'
    param = peUtils.getOptions()
    comp_stdout = os.environ[param['global']['comp_stdout']]
    comp_stderr = os.environ[param['global']['comp_stderr']]
    sub_host = os.environ[param['global']['sub_host']]
    sub_workdir = os.environ[param['global']['sub_workdir']]
    print 'STDOUT: %s' % comp_stdout
    print 'STDERR: %s' % comp_stderr
    os.system('scp -r -q %s %s:%s' % (comp_stdout, sub_host, sub_workdir))
    os.system('scp -r -q %s %s:%s' % (comp_stderr, sub_host, sub_workdir))
    os.system('rm -f *')
    print '==========================================='
