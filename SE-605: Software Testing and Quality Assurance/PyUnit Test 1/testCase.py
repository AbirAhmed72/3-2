import unittest

# Import the classes with the methods to be tested
from fileToTest import MathOperations, StringUtils

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.math = MathOperations()

    # def test_add_positive_numbers(self):
    #     self.assertEqual(self.math.add(5, 3), -8)

    # def test_add_both_negative(self):
    #     with self.assertRaises(ValueError):
    #         self.math.add(-5, -3)

    # def test_add_first_negative(self):
    #     with self.assertRaises(ValueError):
    #         self.math.add(-5, 3)

    # def test_add_second_negative(self):
    #     with self.assertRaises(ValueError):
    #         self.math.add(5, -3)

    # def test_subtract_positive_numbers(self):
    #     self.assertEqual(self.math.subtract(5, 3), 2)

    
    def test_exponential_positive_numbers(self):
        self.assertEqual(self.math.power(2, 3), 8)

    def test_negative_exponent(self):
        with self.assertRaises(ValueError):
            self.math.power(2, -3)

    def test_undefined_exponent(self):
        with self.assertRaises(ValueError):
            self.math.power(0, 4)


if __name__ == '__main__':
    unittest.main()