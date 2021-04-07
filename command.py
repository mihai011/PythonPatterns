from unittest import TestCase
from abc import ABC, abstractmethod


class TestCommand(TestCase):

    def test_command(self):

        receiver = Receiver()

        c1 = Command1(receiver)
        c2 = Command2(receiver)

        invoker = Invoker()
        invoker.register("1", c1)
        invoker.register("2", c2)

        self.assertEqual(invoker.send_command("1"), "Control 1")
        self.assertEqual(invoker.send_command("2"), "Control 2")

        with self.assertRaises(NotImplementedError):

            invoker.send_command("3")


class Command(ABC):

    def __init__(self, receiver):

        self.receiver = receiver

    @abstractmethod
    def execute(self):

        raise NotImplementedError()


class Command1(Command):

    def execute(self):

        return self.receiver.run_command1()

class Command2(Command):

    def execute(self):

        return self.receiver.run_command2()

class Receiver():

    @staticmethod
    def run_command1():

        return "Control 1"

    @staticmethod
    def run_command2():

        return "Control 2"

class Invoker():

    def __init__(self):

        self.commands = {}

    def register(self, name , command):

        self.commands[name] = command

    def send_command(self, name):

        if name not in self.commands:
            raise NotImplementedError()

        return self.commands[name].execute()










