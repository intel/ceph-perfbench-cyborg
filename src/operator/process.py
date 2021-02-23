import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from configurator.manager import ConfigurationManager
from executor.manager import ExecutionManager
from analyzer.manager import AnalysisManager

class ProcessManager(object):
    def __init__(self):
        self.cm = ConfigurationManager()
        self.em = ExecutionManager(self.cm)
        self.am = AnalysisManager()

    def load_config(self):
        self.cm.read_config()
        self.cm.parse_config()
        self.em.parse_config()

    def setup(self):
        self.em.setup()
        self.am.setup()

    def run(self):
        self.em.run()
        while self.em.is_completed():
            self.am.run()
            break
