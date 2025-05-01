import unittest
from kursinis import DecimalToRoman, RomanToDecimal, ConverterApp
class TestSimple(unittest.TestCase):
    def test_decimal_to_roman(self):
        converter = DecimalToRoman()
        result = converter.convert_to(11)
        print("\nDecimal 11 =>", result)
        self.assertEqual(result, 'XI')

    def test_roman_to_decimal(self):
        converter = RomanToDecimal()
        result = converter.convert_to('XIV')
        print("\nRoman 'XIV' =>", result)
        self.assertEqual(result, 14)
if __name__ == '__main__': 
    unittest.main(verbosity=2)
