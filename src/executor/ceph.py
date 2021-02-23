from common.utils import CBCLogger

import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from executor.executor import Executor

class CephExecutor(Executor):
    def __init__(self, config_obj):
        self.config_obj = config_obj

    def build(self):
        CBCLogger.debug("Build Ceph source code.")

    def setup(self):
        CBCLogger.debug("Setup and deploy Ceph cluster.")

    def run(self):
        CBCLogger.debug("Run Ceph cluster.")
    
    def cleanup(self):
        CBCLogger.debug("Clean up the cluster.")

