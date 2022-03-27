import unittest

class Calculator(object):

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        '''Test funkcji dodawania'''
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test funkcji odejmowania'''
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    def test_mul(self):
        '''Test funkcji mnożenia'''
        self.calc = Calculator()
        result = self.calc.mul(3, 8)
        expected = 24
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test funkcji dzielenia'''
        self.calc = Calculator()
        result = self.calc.div(15, 3)
        expected = 5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2)