from abc import ABC, abstractmethod
from unittest import TestCase

class TestFacade(TestCase):

    def test_machine(self):

        self.assertTrue(all(RealMachine.run()))


class Component(ABC):

    def test(self):

        return True

class Engine(Component):
    pass

class Chassis(Component):
    pass

class Wheels(Component):
    pass


class Machine(ABC):

    @classmethod
    def run(cls):

        status_engine = cls._engine.test()
        status_chassis = cls._chassis.test()
        status_wheels = cls._wheels.test()

        return [status_engine, status_wheels, status_chassis]


class RealMachine(Machine):

    _engine = Engine()
    _chassis = Chassis()
    _wheels = Wheels()
