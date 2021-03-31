from abc import ABC, abstractmethod
from unittest import TestCase
from enum import Enum, auto

class TestChain(TestCase):

    def test_chain(self):

        coal_engine = FossilEngine([EnergySource.coal])
        gas_engine = FossilEngine([EnergySource.gas])

        electric_mana_engine = FutureEngine([EnergySource.electricity, EnergySource.mana])

        #make chain

        gas_engine.set_link(electric_mana_engine)
        coal_engine.set_link(gas_engine)

        self.assertEqual(coal_engine.search(EnergySource.mana),  "Macking power from source:EnergySource.mana")
        with self.assertRaises(NotImplementedError):
            electric_mana_engine.search(EnergySource.gas)


        

class EnergySource(Enum):
    """ Log Levels Enum."""
    gas = auto()
    coal = auto()
    electricity = auto()
    mana = auto()


class Engine(ABC):

    def __init__(self, sources):

        self.sources = sources

        self.link = None

    def set_link(self, link):

        self.link = link

    def search(self, source):

        if source in self.sources:
            return self.power(source)
        else:
            if self.link != None:
                return self.link.search(source)

        raise NotImplementedError()

    @abstractmethod
    def power(self, source):


        raise NotImplementedError


class FossilEngine(Engine):

    def power(self, source):

        return "Macking power from source:{}".format(source)

class FutureEngine(Engine):

    def power(self, source):

        return "Macking power from source:{}".format(source)