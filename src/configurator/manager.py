import argparse
import yaml
from enum import Enum

import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from configurator.benchmark import *
from configurator.platform import *

from common.utils import CBCLogger

config_map = {
    'ceph': 'CephConfigurator',
    'fio': 'FioConfigurator',
    'cosbench': 'CosbenchConfigurator',
    'dstat': 'DstatConfigurator'
}


CONFIG_YAML = "../../config/CBC.yaml"

class ConfigurationManager(object):
    def __init__(self):
        self.config_file = CONFIG_YAML
        self.config_yaml = {}
        self.config_objs = []
    
    def read_config(self):
        try:
            with open(self.config_file) as f:
                self.config_yaml = yaml.safe_load(f)
                print(self.config_yaml)
                CBCLogger.debug("Read config file.")
        except IOError as e:
            raise argparse.ArgumentTypeError(str(e))

    def parse_config(self):
        for i in config_map:
            object_value = self.config_yaml.get(i)
            if object_value != None:
                self.config_objs.append(globals()[config_map.get(i)](object_value))
        print(self.config_objs)
        CBCLogger.debug("Parse config file.")
