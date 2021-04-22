from abc import ABC, abstractmethod
from unittest import TestCase

class TestTemplate(TestCase):

    def test_template(self):

        c = Control()

        self.assertEqual(c.start(), "Control")

        with self.assertRaises(NotImplementedError):
            c.end()


class Game(ABC):

    def __init__(self):

        raise NotImplementedError()

    def start(self):

        raise NotImplementedError()

    def end(self):

        raise NotImplementedError()

class Control(Game):

    def __init__(self):

        self.game = "Control"


    def start(self):

        return self.game

