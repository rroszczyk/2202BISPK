from math import pi
import unittest
from area import *

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_value(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, "s")


if __name__ == "__main__":
    unittest.main()