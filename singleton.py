import random
from unittest import TestCase

class TestSingleton(TestCase):

    def test_singleton_exception(self):

        with self.assertRaises(Exception):
            s1 = Singleton()
            s2 = Singleton()

    
    def test_singleton_simple(self):

        s = Singleton()

        self.assertEqual(s.control, Singleton.instance.control)

    def tearDown(self):

        Singleton.del_instance()

    

class Singleton:

    instance = None

    @staticmethod
    def get_instance():

        if Singleton.instance == None:
            Singleton()

        return instance

    @staticmethod
    def del_instance():

        Singleton.instance = None

    def __init__(self):

        if Singleton.instance == None:
            self.control = random.random()
            Singleton.instance = self
        else:
            raise Exception("Singleton!")




        

