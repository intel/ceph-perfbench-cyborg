
from enum import Enum

class ExecState(Enum):
    Init = 1
    Configured = 2
    Running = 3
    Completed = 4

class Executor(object):
    def __init__(self):
        self.status = ExecState.Init
