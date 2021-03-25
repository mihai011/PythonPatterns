from abc import ABC, abstractmethod
from unittest import TestCase

class TestDecorator(TestCase):

    def test_decorator(self):

        self.ec = ElectricCar()
        self.ecd  = ElectricDecorator(self.ec)

        self.final = ElectricMachineDecorator(self.ecd)

        self.assertTrue(self.final.run())



class Machine(ABC):

    @abstractmethod
    def run(self):

        raise NotImplemented

class ElectricCar(Machine):

    def run(self):

        return "Electric Car"

class ElectricDecorator(Machine):

    def __init__(self, machine):

        self.machine = machine

    def run(self):

        return self.machine.run()

class ElectricMachineDecorator(ElectricDecorator):

    def __init__(self, machine):

        self.machine = machine

    def run(self):

        self.machine.run()
        return self.extra()
    
    def extra(self):

        return True
