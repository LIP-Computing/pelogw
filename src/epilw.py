#!/usr/bin/python

'''
Epilog wrapper for docker images submission to batch systems

Created on Oct 28, 2015

@author: mariojmdavid@gmail.com
'''

import time
from optparse import OptionParser
import ConfigParser
import os
import errno
import confParam


def getOptions():
    parser = OptionParser()
    parser.add_option('-c', '--conf', dest='filename',
                      help='Configuration file.\nDefault: cont-batch.conf',
                      metavar='[ConfigFile]')
    (options, args) = parser.parse_args()
    confFile = '/opt/ge-tools/exec/david/etc/cont-batch.conf'
    if (options.filename):  # TODO: check if conf file exists
        confFile = options.filename
    param = readConf(confFile)
    return param


def readConf(confFile):
    ''' Reads the configuration file
    Sets the parameters into self.confParam structure
    '''
    config = ConfigParser.ConfigParser(allow_no_value=True)
    config.read(confFile)
    print 'Using config file: %s' % confFile
    cfp = confParam.ConfigParameters()
    confPar = cfp.getBaseConf()
    for section in confPar:
        for param in confPar[section]:
            try:
                confPar[section][param] = config.get(section, param)
            except:
                print 'Default value section=%s  %s = %s' % \
                    (section, param, confPar[section][param])
    return confPar

if __name__ == '__main__':
    print '==========================================='
    print '==========================================='
    ti = time.time()
    print 'I am the EPILOG'
    param = getOptions()
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
