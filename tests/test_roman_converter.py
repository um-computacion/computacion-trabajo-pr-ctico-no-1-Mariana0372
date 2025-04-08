import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



from roman_converter import decimal_to_roman

import unittest


class TestRomanConverter(unittest.TestCase):
    
    def test_single_digits(self):
        """Test conversion of single digit numbers"""
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(7), "VII")
        self.assertEqual(decimal_to_roman(8), "VIII")
        self.assertEqual(decimal_to_roman(9), "IX")
    
    def test_tens(self):
        """Test conversion of tens"""
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(20), "XX")
        self.assertEqual(decimal_to_roman(30), "XXX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(60), "LX")
        self.assertEqual(decimal_to_roman(70), "LXX")
        self.assertEqual(decimal_to_roman(80), "LXXX")
        self.assertEqual(decimal_to_roman(90), "XC")
    
    def test_hundreds(self):
        """Test conversion of hundreds"""
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(200), "CC")
        self.assertEqual(decimal_to_roman(300), "CCC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(600), "DC")
        self.assertEqual(decimal_to_roman(700), "DCC")
        self.assertEqual(decimal_to_roman(800), "DCCC")
        self.assertEqual(decimal_to_roman(900), "CM")
    
    def test_thousands(self):
        """Test conversion of thousands"""
        self.assertEqual(decimal_to_roman(1000), "M")
        self.assertEqual(decimal_to_roman(2000), "MM")
        self.assertEqual(decimal_to_roman(3000), "MMM")
    
    def test_combined_numbers(self):
        """Test conversion of combined numbers"""
        self.assertEqual(decimal_to_roman(14), "XIV")
        self.assertEqual(decimal_to_roman(42), "XLII")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(246), "CCXLVI")
        self.assertEqual(decimal_to_roman(789), "DCCLXXXIX")
        self.assertEqual(decimal_to_roman(1999), "MCMXCIX")
        self.assertEqual(decimal_to_roman(2023), "MMXXIII")
        self.assertEqual(decimal_to_roman(3549), "MMMDXLIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Minimum value
        self.assertEqual(decimal_to_roman(1), "I")
        # Maximum value
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")
    
    def test_invalid_inputs(self):
        """Test invalid inputs"""
        # Below range
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        
        # Above range
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)
        
        # Negative numbers
        with self.assertRaises(ValueError):
            decimal_to_roman(-1)
        
        # Non-integer inputs
        with self.assertRaises(TypeError):
            decimal_to_roman("not a number")
        
        with self.assertRaises(TypeError):
            decimal_to_roman(3.14)

if __name__ == "__main__":
    unittest.main()