from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def method1(self):

        pass

    @abstractmethod
    def method2(self):

        pass

class ConcreteClass(AbstractClass):

    def method1(self)->str:

        return "Not implemented!"

    def method2(self)->str:

        return "Not implemented!"

