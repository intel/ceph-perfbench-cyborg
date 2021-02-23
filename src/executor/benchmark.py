from common.utils import CBCLogger

import sys, os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from executor.executor import Executor

class BenchmarkExecutor(Executor):
    def __init__(self):
        pass

class FioExecutor(BenchmarkExecutor):
    def __init__(self, config_obj):
        self.config_obj = config_obj

    def build(self):
        CBCLogger.debug("Build Fio source code.")
    
    def setup(self):
        CBCLogger.debug("Setup Fio.")
    
    def run(self):
        CBCLogger.debug("Run Fio Start.")
        time.sleep(10)
        CBCLogger.debug("Run Fio End.")
