import unittest
from int_roman import *


class TestRomanInt(unittest.TestCase):
    def test_is_zero(self):
        result = int_to_roman(0)
        self.assertEqual(result, '')

    # def test_is_int(self):
    #     result = int_to_roman(a)
    #     self.assertEqual(result, '')

    def test_roman_to_decimal(self):
        result = int_to_roman(1)
        self.assertEqual(result, 'I')

    # def test_is_not_negative(self):
    #     result = int_to_roman(-1)
    #     self.assertEqual(result, '')
        
    # def test_is_minor_3000(self):
    #     result = int_to_roman(3001)
    #     self.assertEqual(result, '')


if __name__ == "__main__":
    unittest.main()

