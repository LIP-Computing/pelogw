#########################################################################
# Developed in the framework of INDIGO project,
#
# Author: Mario David <mariojmdavid@gmail.com>
#########################################################################
'''
Class that defines all configuration parameters
and can write a config template

Created on Oct 28, 2015

@author: mariojmdavid@gmail.com
'''


class ConfigParameters(object):
    def __init__(self):
        self.allParam = {'global': {}}
        self.allParam['global']['batch_sys'] = ''
        self.allParam['global']['log_level'] = 'INFO'
        self.allParam['global']['base_dir'] = ''
        self.allParam['global']['log_dir'] = '/var/log'
        self.allParam['global']['log_file'] = ''
        self.allParam['global']['job_name'] = ''
        self.allParam['global']['job_id'] = ''
        self.allParam['global']['job_script'] = ''
        self.allParam['global']['sub_host'] = ''
        self.allParam['global']['sub_user'] = ''
        self.allParam['global']['sub_workdir'] = ''
        self.allParam['global']['comp_host'] = ''
        self.allParam['global']['comp_user'] = ''
        self.allParam['global']['comp_home'] = ''
        self.allParam['global']['comp_stdin'] = ''
        self.allParam['global']['comp_stdout'] = ''
        self.allParam['global']['comp_stderr'] = ''

    def _composeWrt(self):
        confp = ['# Config file for prolog and epilog of a given batch system']
        confp.append('# uncommented options are mandatory')
        confp.append('# commented options have the default value\n')
        # Section global
        confp.append('[global]\n')
        confp.append('#')
        confp.append('# Global configuration options')
        confp.append('#\n')
        return confp

    def writeTpl(self, fname='cont-batch.conf.template'):
        cfg = self._composeWrt()
        with open(fname, 'w') as of:
            for l in cfg:
                of.write(l)

    def getBaseConf(self):
        return self.allParam
