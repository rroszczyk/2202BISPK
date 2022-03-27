import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "wynik poprawyn to 6"

    def test_sum_tuple(self):
        assert sum((1, 2, 2)) == 6, "wynik poprawyn to 6"


if __name__ == "__main__":
    unittest.main()