import unittest

# so yeah, added at least one test here

def fun(x):
    return x + 1

class AdditionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)