class MathOperations:

    def add(self, a, b):
        if a < 0 and b < 0:
            raise ValueError("Both input values are negative")
        elif a < 0:
            raise ValueError("The first input value is negative")
        elif b < 0:
            raise ValueError("The second input value is negative")
        return a + b

    def subtract(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Input values must be non-negative")
        elif a < b:
            raise ValueError("Cannot subtract a larger value from a smaller one")
        return a - b

    def multiply(self, a, b):
        if (a == 0 and b != 0) or (a != 0 and b == 0):
            return 0
        elif a == 0 and b == 0:
            raise ValueError("Both input values are zero")
        return a * b

    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Division by zero is not allowed")
        elif dividend % divisor != 0:
            raise ValueError("Division does not result in an integer")
        return dividend / divisor

    def power(self, base, exponent):
        if exponent < 0:
            raise ValueError("Exponent must be non-negative")
        elif base == 0 and exponent == 0:
            raise ValueError("0^0 is undefined")
        result = 1
        for i in range(exponent):
            result *= base
        return result
    


class StringUtils:

    def concatenate(self, str1, str2):
        if str1 is None or str2 is None:
            raise ValueError("Input strings must not be None")
        elif len(str1) == 0 and len(str2) == 0:
            raise ValueError("Both input strings are empty")
        return str1 + str2

    def calculate_length(self, str):
        if str is None:
            raise ValueError("Input string must not be None")
        elif len(str.strip()) == 0:
            raise ValueError("Input string contains only whitespace characters")
        return len(str)

    def contains_substring(self, str, substr):
        if str is None or substr is None:
            raise ValueError("Input strings must not be None")
        elif len(str) < len(substr):
            raise ValueError("The substring is longer than the input string")
        return substr in str

    def to_upper_case(self, str):
        if str is None:
            raise ValueError("Input string must not be None")
        elif len(str) > 100:
            raise ValueError("Input string is too long for processing")
        return str.upper()

    def trim_whitespace(self, str):
        if str is None:
            raise ValueError("Input string must not be None")
        elif len(str) < 5:
            raise ValueError("Input string is too short for trimming")
        return str.strip()