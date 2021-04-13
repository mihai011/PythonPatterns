from unittest import TestCase

class TestIter(TestCase):

    def test_iter(self):

        iterator = iter(Trivial(0))
        m = [i for i in iterator]
        sure = [i for i in range(1, 200)]

        self.assertEqual(m , sure)

class Trivial():

    def __init__(self, val):

        self.val = val

    def __iter__(self):

        return self

    def __next__(self):

        if self.val < 199: 
            self.val += 1
            return self.val
        else:
            raise StopIteration