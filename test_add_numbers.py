import unittest
import io
import sys
from unittest.mock import patch
from add_numbers import add_two_numbers, main

class TestAddNumbers(unittest.TestCase):
    
    def test_add_two_positive_integers(self):
        """Test adding two positive integers"""
        result = add_two_numbers(5, 3)
        self.assertEqual(result, 8)
        
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        result = add_two_numbers(-5, -7)
        self.assertEqual(result, -12)
        
    def test_add_positive_and_negative(self):
        """Test adding a positive and negative number"""
        result = add_two_numbers(10, -4)
        self.assertEqual(result, 6)
        
    def test_add_zero(self):
        """Test adding zero to a number"""
        result = add_two_numbers(8, 0)
        self.assertEqual(result, 8)
        
    def test_add_floats(self):
        """Test adding floating point numbers"""
        result = add_two_numbers(3.5, 2.5)
        self.assertEqual(result, 6.0)
        
    def test_add_large_numbers(self):
        """Test adding large numbers"""
        result = add_two_numbers(999999, 1)
        self.assertEqual(result, 1000000)
    
    @patch('builtins.input', side_effect=['10', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_function_valid_input(self, mock_stdout, mock_input):
        """Test main function with valid inputs"""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("The sum of 10.0 and 5.0 is: 15.0", output)
    
    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_function_invalid_input(self, mock_stdout, mock_input):
        """Test main function with invalid input"""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Please enter valid numbers", output)

if __name__ == '__main__':
    unittest.main()
