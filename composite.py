from abc import ABC, abstractmethod
from unittest import TestCase 

class TestNodes(TestCase):

    def test_nodes(self):

        self.comp = Composite()
        self.p = Composite()
        self.comp.set_parent(self.p)

        self.assertEqual(self.comp.get_parent(), self.p)



class Node(ABC):


    def get_nodes(self):

        return self.nodes


    def get_parent(self):

        return self.parent 


    def set_parent(self, parent):

        self.parent = parent

    def add_nodes(self, node):

        self.nodes.append(node)

class Composite(Node):

    def __init__(self):

        self.parent = None
        self.nodes = []





