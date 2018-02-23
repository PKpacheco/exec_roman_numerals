import unittest
from roman_int import roman_to_int


class TestIntRoman(unittest.TestCase):
    def test_is_roman(self):
        result = roman_to_int("X")
        self.assertEqual(result, 10)

    def test_is_roman(self):
        result = roman_to_int("C")
        self.assertEqual(result, 100)

    
if __name__ == "__main__":
    unittest.main()
