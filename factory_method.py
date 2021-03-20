from abc import ABC, abstractmethod
from unittest import TestCase

class TestVehicles(TestCase):

    def test_electric_light_vehicle(self):

        vehicle = ElectricLightVehicle()

        vehicle.get_engine()
        vehicle.get_chasis()

        self.assertEqual(vehicle.test_vehicle(),"Tested Electric Engine"+"Tested Light Chasis")


class Engine(ABC):

    @abstractmethod
    def test(self):

        raise NotImplementedError

class ElectricEngine(Engine):

    def test(self):
        return "Tested Electric Engine"

class GasEngine(Engine):

    def test(self):
        return "Tested Gas Engine"

class Chasis(ABC):

    @abstractmethod
    def test(self):

        raise NotImplementedError

class LightChasis(Chasis):

    def test(self):

        return "Tested Light Chasis"

class HeavyChasis(Chasis):

    def test(self):

        return "Tested Heavy Chasis"


class Vehicle(ABC):

    def __init__(self):

        self.motor = None
        self.chasis = None

    @abstractmethod
    def get_engine(self):

        return NotImplementedError
    
    @abstractmethod
    def get_chasis(self):

        return NotImplementedError

    def test_vehicle(self):

        status_engine = self.engine.test()
        status_chasis = self.chasis.test()

        return status_engine + status_chasis

class ElectricLightVehicle(Vehicle):

    def get_engine(self):

        self.engine = ElectricEngine()

    def get_chasis(self):

        self.chasis = LightChasis()

class GasHeavyVehicle(Vehicle):

    def get_engine(self):

        self.engine = GasEngine()

    def get_chasis(self):

        self.chasis = HeavyChasis()








