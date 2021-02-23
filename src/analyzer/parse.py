import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from analyzer.analyzer import *
from common.utils import CBCLogger

class DataParser(Analyzer):
    def __init__(self):
        pass

    def build(self):
        CBCLogger.debug("Build Parser source code.")

    def setup(self):
        CBCLogger.debug("Setup Parser.")

    def run(self):
        CBCLogger.debug("Run Parser.")
    
    def check_bottleneck(self):
        CBCLogger.debug("Check bottleneck is in Ceph.")
        return True
