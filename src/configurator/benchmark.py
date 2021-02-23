
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from configurator.configurator import *

class BenchmarkConfigurator(Configurator):
    def __init__(self):
        pass

class FioConfigurator(BenchmarkConfigurator):
    def __init__(self, config):
        self.vol_size = 1
        self.vol_num = 1
        self.warmup = 1
        self.runtime = 1
        self.qd_list = 1
        self.qd_pick = Pick.BestBW
        self.blk_size = 1
        self.threads = 1
        self.direct = 1
        self.engine = 1


