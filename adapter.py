from abc import ABC, abstractmethod
from unittest import TestCase

class TestMachine(TestCase):

    def test_machine_classic_engine(self):

        engine = ClassicEngine()
        machine = NewMachine(engine)
        self.assertEqual(machine.construct(), "Made car with engine!" )

    def test_machine_new_engine(self):

        engine = NewEngine()
        machine = NewMachine(engine)
        self.assertEqual(machine.construct(), "Can't make car with power greater than 150!")

    def test_machine_adapter(self):

        engine = NewEngine()
        adapter = Adapter(engine)
        machine = NewMachine(adapter)
        self.assertEqual(machine.construct(), "Made car with engine!" )


class Machine(ABC):

    def __init__(self, engine):

        self.engine = engine

    @abstractmethod
    def construct():

        raise NotImplementedError


class Engine(ABC):

    def power(self):

        return self.output


class ClassicEngine(Engine):

    def __init__(self):

        self.output = 150

class NewEngine(Engine):

    def __init__(self):

        self.output = 200

class NewMachine(Machine):

    def construct(self):

        if self.engine.power() > 150:
            return "Can't make car with power greater than 150!"
        else:
            return "Made car with engine!"

class Adapter(Engine):

    def __init__(self, engine):

        self.output = engine.output - 50
