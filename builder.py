from abc import ABC, abstractmethod
from unittest import TestCase


class TestExecutor(TestCase):

    def test_exect(self):

        rec = ConcreteRecipe()
        rec.recipe = "French Fries"

        ex = ConcreteExecutor()
        ex.register(rec)
        ex.make_execute()
        
        self.assertEqual(rec.recipe, "Executed {}".format("French Fries"))


class AbstractExecutor(ABC):

    @abstractmethod
    def register(self):

        raise NotImplementedError

class AbstractRecipe(ABC):

    @abstractmethod
    def recipe(self):

        raise NotImplementedError

    @abstractmethod
    def execute_recipe(self):

        raise NotImplementedError

class ConcreteRecipe(AbstractRecipe):

    def __init__(self):
        self.recipe = None

    def recipe(self, recipe:str):
        self.recipe = recipe

    def execute_recipe(self):

        self.recipe = "Executed {}".format(self.recipe)

class ConcreteExecutor(AbstractExecutor):

    def __init__(self):

        self.recipe = None

    def register(self, recipe):

        self.recipe = recipe 

    def make_execute(self):

        self.recipe.execute_recipe()

    