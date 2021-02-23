
import sys, os
import time
import threading
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from executor.executor import *
from executor.ceph import CephExecutor
from executor.benchmark import FioExecutor
from executor.platform import DstatExecutor

from common.utils import CBCLogger

execute_map = {
    'CephConfigurator': 'CephExecutor',
    'FioConfigurator': 'FioExecutor',
    'DstatConfigurator': 'DstatExecutor'
}

class ExecutionManager(object):
    def __init__(self, config_manager):
        self.cm = config_manager
        self.exec_objs = []
        self.benchmarks = []
        self.parallels = []
        self.state = ExecState.Init

    def parse_config(self):
        for i in execute_map:
            for j in self.cm.config_objs:
                if j.__class__.__name__ == i:
                    #print(globals()[execute_map.get(i)])
                    self.exec_objs.append(globals()[execute_map.get(i)](j))
        print(self.exec_objs)
    
    def setup(self):
        for i in self.exec_objs:
            i.build()
            time.sleep(1)
            i.setup()
            time.sleep(1)
        self.state = ExecState.Configured

    def is_completed(self):
        return self.state == ExecState.Completed

    # Run model:
    #   Ceph cluster run as daemon
    #   Benchmarks run in one by one
    #   Tools run in parallel
    def run(self):
        CBCLogger.debug("Executor start to run.")
        for i in self.exec_objs:
            #CBCLogger.debug("Iterate execute obj:"+i.__class__.__name__+",parent obj:"+i.__class__.__bases__[0].__name__)
            if i.__class__.__bases__[0].__name__ == 'BenchmarkExecutor':
                #mrunner = BenchThread(i)
                #mrunner.start()
                self.benchmarks.append(i)
            elif i.__class__.__bases__[0].__name__ == 'ToolExecutor':
                #i.run()
                self.parallels.append(i)
        
        mrunner = MainThread(self.benchmarks, self.parallels)
        mrunner.start()
        self.state = ExecState.Running
        mrunner.join()
        self.state = ExecState.Completed

class MainThread(threading.Thread):
    def __init__(self, benchmarks, parallels):
        threading.Thread.__init__(self)
        self.benchmarks = benchmarks
        self.parallels = parallels
    
    def run(self):
        CBCLogger.debug("Run Benchmark in another thread.")
        for i in self.benchmarks:
            for j in self.parallels:
                j.run()
            i.run()
        CBCLogger.debug("Run Benchmarks Done.")
        