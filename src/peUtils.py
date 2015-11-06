'''
Utils functions for prologue and epilogue wrapers

Created on Nov 06, 2015

@author: mariojmdavid@gmail.com
'''

from optparse import OptionParser
import ConfigParser
import sys
import confParam


def getOptions():
    parser = OptionParser()
    parser.add_option('-c', '--conf', dest='filename',
                      help='Configuration file.\n \
                          Default: /etc/pelogw/cont-batch.conf',
                      metavar='[ConfigFile]')
    (options, args) = parser.parse_args()
    confFile = '/etc/pelogw/cont-batch.conf'
    if (options.filename):
        confFile = options.filename
    try:
        f = open(confFile, 'r')
        f.close()
    except IOError as e:
        print 'Error in file %s: %s' % (confFile, e)
        sys.exit(1)
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
