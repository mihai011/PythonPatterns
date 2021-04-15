
from unittest import TestCase
from copy import deepcopy


class TestMemento(TestCase):

    def test_memento(self):

        m = Machine(100)
        check = m.save_state()


        m.set_power(200)
        self.assertEqual(m.power, 200)

        m.get_state(check)

        self.assertEqual(m.power, 100)
        

class Memento():

    def __init__(self, state):

        self.state = state
    
class Machine():

    def __init__(self, power):

        self.power = power

    def set_power(self, power):

        self.power = power

    def save_state(self):

        return Memento(deepcopy(self))

    def get_state(self, memento):

        self.power = memento.state.power

    def __str__(self):

        return str(self.power)
