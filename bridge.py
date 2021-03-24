from abc import ABC, abstractmethod
from unittest import TestCase

class Testmachine(TestCase):

    def test_machine(self):

        engine = ElectricEngine()

        machine = MachineEngine(engine)

        self.assertEqual(machine.use_engine(), "Electric Power")

class Machine(ABC):

    def use_engine(self):

        return self.engine.make_power()

class MachineEngine(Machine):

    def __init__(self, engine):

        self.engine = engine


class Engine(ABC):

    @abstractmethod
    def make_power(self):

        raise NotImplementedError


class ElectricEngine(Engine):

    def make_power(self):

        return "Electric Power"