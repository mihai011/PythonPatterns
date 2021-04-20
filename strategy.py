from unittest import TestCase


class TestStrategy(TestCase):

    def test_strategy(self):

        c = Context()
        data_sum = [1,2,3]
        data_join = ['a','b','c']

        self.assertEqual(c.execute(data_sum), 6)

        self.assertEqual(c.execute(data_join), 'abc')
        


class Strategy1():

    def implement(self, data):

        return sum(data)

class Strategy2():

    def implement(self, data):

        return ''.join(data)


class Context():


    def execute(self, data):

        strategy = None
        if type(data[0]) == int:
            strategy  = Strategy1()

        if type(data[0]) == str:
            strategy = Strategy2()


        return strategy.implement(data)



