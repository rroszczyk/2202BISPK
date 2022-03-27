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
        if b == 0:
            raise ZeroDivisionError("Wystąpił błąd dzielenia przez zero")
        return a / b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        '''Konfiguracja środowiska uruchomieniowego przed każdym wywołaniem'''
        self.calc = Calculator()

    def test_add(self):
        '''Test funkcji dodawania'''
        self.assertEqual(self.calc.add(4, 7), 11)
        self.assertEqual(self.calc.add(4, 10), 14)
        self.assertEqual(self.calc.add(3, 7), 10)
        self.assertEqual(self.calc.add(1, 7), 11)
        self.assertEqual(self.calc.add(2, 7), 11)

    def test_sub(self):
        '''Test funkcji odejmowania'''
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    @unittest.skip("Nie testujemy mnożenia")
    def test_mul(self):
        '''Test funkcji mnożenia'''
        result = self.calc.mul(3, 8)
        expected = 24
        self.assertEqual(result, expected)

class TestDivCalculator(unittest.TestCase):

    def setUp(self):
        '''Konfiguracja środowiska uruchomieniowego przed każdym wywołaniem'''
        self.calc = Calculator()

    def test_div(self):
        '''Test funkcji dzielenia'''
        result = self.calc.div(15, 3)
        expected = 5
        self.assertEqual(result, expected)

    def test_div_by_zero(self):
        '''Test funkcji dzielenia przez zero'''
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2)