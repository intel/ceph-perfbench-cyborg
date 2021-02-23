import argparse
import yaml
from enum import Enum

class Pick(Enum):
    All = 0
    BestBW = 1
    BestLat = 2

objects = {
    'ceph': 'CephConfigurator',
    'fio': 'FioConfigurator',
    'cosbench': 'CosbenchConfigurator',
    'dstat': 'StatConfigurator'
}

CONFIG_YAML = "CBC.yaml"

class Configurator(object):
    def __init__(self):
        pass

