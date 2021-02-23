
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from analyzer.parse import DataParser
from analyzer.present import DataPresenter

class AnalysisManager(object):
    def __init__(self):
        self.parser = DataParser()
    
    def setup(self):
        self.parser.build()
        self.parser.setup()

    def run(self):
        self.parser.run()
        self.parser.check_bottleneck()

