import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from common.utils import CBCLogger

from process import ProcessManager
from configurator.manager import ConfigurationManager
from executor.manager import ExecutionManager

class Operator(object):
    def __init__(self):
        self.pm = ProcessManager()

    def run(self):
        self.pm.load_config()
        self.pm.setup()
        self.pm.run()


if __name__ == "__main__":
    op = Operator()
    op.run()