from abc import ABC, abstractmethod
import copy
from unittest import TestCase

class TestClone(TestCase):

    def test_clone(self):

        cl = CloningFacility()
        test = cl.clone()

        self.assertEqual(cl.members, test.members)



class Origin(ABC):

    @abstractmethod
    def method(self):

        raise NotImplementedError

    def clone(self):

        return copy.deepcopy(self)

class CloningFacility(Origin):

    def __init__(self):

        self.members = "Someone"

    def method(self):

        return "Inheritance"


