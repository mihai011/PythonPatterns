from abc import ABC, abstractmethod
from unittest import TestCase


class TestProxy(TestCase):

    def test_proxy(self):

        self.engine = Engine()
        self.machine = MachineProxy(self.engine)

        self.assertTrue(self.machine.operate())


class MachineAbstract(ABC):

    @abstractmethod
    def operate(self):

        raise NotImplementedError("Error")


class Engine():

    def power(self):
        return True

class Chassis():

    def sustain(self):
        return True

class MachineProxy(MachineAbstract):

    def __init__(self, engine):

        self.engine = engine
        self.chassis = Chassis()

    def operate(self):

        if self.engine.power() and self.chassis.sustain():
            return True

        return False

    
        