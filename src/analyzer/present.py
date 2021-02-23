import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from analyzer.analyzer import *

class DataPresenter(Analyzer):
    def __init__(self):
        pass

    def build(self):
        CBCLogger.debug("Build Presenter source code.")

    def setup(self):
        CBCLogger.debug("Setup Presenter.")

    def run(self):
        CBCLogger.debug("Run Presenter.")
