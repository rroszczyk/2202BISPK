import unittest

class WeightValueError(ValueError):
    pass

class HeightValueError(ValueError):
    pass


def calculateBMI(weight, height):
    if weight <= 0:
        raise WeightValueError("Waga powinna być większa od zera")
    if height <= 0:
        raise HeightValueError("Wzrost powinien być większy od zera")
    bmi = weight / (height * height)
    return round(bmi, 2)

class TestCalculateBMI(unittest.TestCase):
    def test_calculateBMI(self):
        bmi = 21.74
        weight = 72
        height = 1.82
        result = calculateBMI(weight, height)
        self.assertEqual(result, bmi)

    def test_calculateWeightError(self):
        bmi = 21.74
        weight = -72
        height = 1.82
        self.assertRaises(WeightValueError, calculateBMI, weight, height)

    def test_calculateHeightError(self):
        bmi = 21.74
        weight = 72
        height = -1.82
        self.assertRaises(HeightValueError, calculateBMI, weight, height)