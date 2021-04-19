from unittest import TestCase
from abc import ABC, abstractmethod


class TestState(TestCase):

    def test_state(self):

        m = Machine()

        m.make('a'*10)
        m.make('b'*10)
        m.make('c'*10)
        m.make('d'*10)
        m.make('e'*10)
        m.make('f'*10)
        m.make('g'*10)
        m.make('h'*10)
        m.make('i'*10)
        m.make('j'*10)
        m.make('k'*10)
        m.make('l'*10)
        m.make('m'*10)
        m.make('n'*10)
        m.make('o'*10)
        m.make('p'*10)


class StateInter(ABC):

    @abstractmethod
    def control(self):

        raise NotImplemented()

class LightState(StateInter):

    def control(self, mechine, s):

        print(s.upper())
        mechine.set_state(HeavyState())



class HeavyState(StateInter):

    passes = 0

    def control(self, machine, s):
        
        print(s.lower())
        if HeavyState.passes == 3:
            machine.set_state(LightState())
            HeavyState.passes = 0
        HeavyState.passes += 1

class Machine():

    def __init__(self):

        self.state = LightState()

    def set_state(self, state):

        self.state = state 

    def make(self, s):

        self.state.control(self, s)
