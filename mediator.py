from abc import ABC, abstractmethod

from unittest import TestCase

class TestMediator(TestCase):

    def test_mediator(self):

        med = Machine()

        node1 = Piece(10, 30)
        node2 = Piece(20, 40)

        med.register(1, node1)
        med.register(2, node2)

        med.comunicate(1, 2)

        self.assertEqual(node1.val, 20)
        self.assertEqual(node2.val, 50)

class AbstractPiece():

    @abstractmethod
    def input(self):

        raise NotImplementedError()

    @abstractmethod
    def output(self):

        raise NotImplementedError()

class Piece(AbstractPiece):

    def __init__(self, rate, val):

        self.rate = rate
        self.val = val

    def input(self, val):

        self.val += val

    def output(self):

        if self.val < self.rate:

            return 0

        self.val -= self.rate

        return self.rate

class AbstractMachine(ABC):

    @abstractmethod
    def comunicate(self):

        raise NotImplementedError()

    @abstractmethod
    def register(self):

        raise NotImplementedError()

class Machine(AbstractMachine):

    def __init__(self):

        self.nodes = {}

    def register(self, index, node):

        self.nodes[index] = node

    def comunicate(self, node1, node2):

        if node1 not in self.nodes or node2 not in self.nodes:

            return "One of the nodes is not there!"

        o = self.nodes[node1].output()
        self.nodes[node2].input(o)

        return o

    

