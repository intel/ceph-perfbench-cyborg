
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from configurator.configurator import Configurator

class CephConfigurator(Configurator):
    def __init__(self, config):
        pass

class DstatConfigurator(Configurator):
    def __init__(self, config):
        pass