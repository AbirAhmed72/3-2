import unittest

from fileToTest import MathOperations, StringUtils

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.math = MathOperations()

    #Addition tests: 4 independent paths
    def test_add_positive_numbers(self):
        self.assertEqual(self.math.add(5, 3), 8)

    def test_add_both_negative(self):
        with self.assertRaises(ValueError):
            self.math.add(-5, -3)

    def test_add_first_negative(self):
        with self.assertRaises(ValueError):
            self.math.add(-5, 3)

    def test_add_second_negative(self):
        with self.assertRaises(ValueError):
            self.math.add(5, -3)

    #Subtraction tests: 3 independent paths
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.math.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.math.subtract(-3, -5)

    def test_subtract_negative_result(self):
        with self.assertRaises(ValueError):
            self.math.subtract(3, 5)
    
    #Multiplication tests: 4 independent paths
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.math.multiply(5, 3), 15)

    def test_multiply_by_zero(self):
        self.assertEqual(self.math.multiply(5, 0), 0)

    def test_multiply_zero(self):
        self.assertEqual(self.math.multiply(0, 5), 0)

    def test_multiply_both_zero(self):
        with self.assertRaises(ValueError):
            self.math.multiply(0, 0)

    #Division tests: 3 independent paths
    def test_divide_valid_values(self):
        self.assertEqual(self.math.divide(15, 3), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.divide(5, 0)

    def test_division_not_integer(self):
        with self.assertRaises(ValueError):
            self.math.divide(5, 2)

    #Exponential tests: 4 independent paths
    def test_exponential_positive_numbers(self):
        self.assertEqual(self.math.power(2, 3), 8)

    def test_negative_exponent(self):
        with self.assertRaises(ValueError):
            self.math.power(2, -3)

    def test_undefined_exponent(self):
        with self.assertRaises(ValueError):
            self.math.power(0, 0)


class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.string_utils = StringUtils()

    #Concatenation tests: 3 independent paths
    def test_concatenate_strings(self):
        self.assertEqual(self.string_utils.concatenate("Hello, ", "World!"), "Hello, World!")

    def test_concatenate_None_strings(self):
        with self.assertRaises(ValueError):
            self.string_utils.concatenate(None, None)

    def test_concatenate_empty_strings(self):
        with self.assertRaises(ValueError):
            self.string_utils.concatenate("", "")

    #Length tests: 3 independent paths
    def test_calculate_length(self):
        self.assertEqual(self.string_utils.calculate_length("Python"), 6)

    def test_calculate_length_None_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.calculate_length(None)

    def test_calculate_length_empty_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.calculate_length("   ")

    #Substring tests: 3 independent paths
    def test_contains_substring(self):
        self.assertTrue(self.string_utils.contains_substring("Python is great", "is"))

    def test_contains_None_substring(self):
        with self.assertRaises(ValueError):
            self.string_utils.contains_substring("Hello", None)

    def test_contains_longer_substring(self):
        with self.assertRaises(ValueError):
            self.string_utils.contains_substring("Hello", "Hello, World!")

    #UpperCase tests: 3 independent paths
    def test_to_upper_case(self):
        self.assertEqual(self.string_utils.to_upper_case("hello"), "HELLO")

    def test_to_upper_case_None_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.to_upper_case(None)

    def test_to_upper_case_long_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.to_upper_case("a" * 101)

    #TrimSpace tests: 3 independent paths
    def test_trim_whitespace(self):
        self.assertEqual(self.string_utils.trim_whitespace("   Python   "), "Python")

    def test_trim_whitespace_None_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.trim_whitespace(None)

    def test_trim_whitespace_short_string(self):
        with self.assertRaises(ValueError):
            self.string_utils.trim_whitespace("abc")

if __name__ == '__main__':
    unittest.main()