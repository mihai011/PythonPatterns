from abc import ABC, abstractmethod
from unittest import TestCase

class TestAbstract(TestCase):

    def test_concrete(self):

        co = ConcreteClass()
        self.assertEqual("Not implemented!", co.method1())
        self.assertEqual("Not implemented!", co.method2())


class AbstractClass(ABC):

    @abstractmethod
    def method1(self):

        raise NotImplementedError

    @abstractmethod
    def method2(self):

        raise NotImplementedError

class ConcreteClass(AbstractClass):

    def method1(self)->str:

        return "Not implemented!"

    def method2(self)->str:

        return "Not implemented!"