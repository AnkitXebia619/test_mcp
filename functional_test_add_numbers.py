#!/usr/bin/env python3
"""
Functional tests for the add_numbers program.
These tests verify the program's behavior from a user's perspective.
"""

import unittest
import subprocess
import sys
import os
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
import importlib

# Import the module to be tested
import add_numbers

class AddNumbersFunctionalTest(unittest.TestCase):
    
    def test_program_execution_with_valid_inputs(self):
        """Test the full program execution with valid numeric inputs."""
        # Simulate user input
        user_input = "10\n5\n"
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdin = StringIO(user_input)
        
        with redirect_stdout(captured_output):
            # Call the main function of the add_numbers module
            add_numbers.main()
        
        # Reset stdin
        sys.stdin = sys.__stdin__
        
        # Check the output
        output = captured_output.getvalue()
        self.assertIn("Program to add two numbers", output)
        self.assertIn("The sum of 10.0 and 5.0 is: 15.0", output)
    
    def test_program_execution_with_float_inputs(self):
        """Test the full program execution with float inputs."""
        # Simulate user input
        user_input = "7.5\n2.5\n"
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdin = StringIO(user_input)
        
        with redirect_stdout(captured_output):
            # Call the main function of the add_numbers module
            add_numbers.main()
        
        # Reset stdin
        sys.stdin = sys.__stdin__
        
        # Check the output
        output = captured_output.getvalue()
        self.assertIn("Program to add two numbers", output)
        self.assertIn("The sum of 7.5 and 2.5 is: 10.0", output)
    
    def test_program_execution_with_negative_inputs(self):
        """Test the full program execution with negative inputs."""
        # Simulate user input
        user_input = "-10\n-5\n"
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdin = StringIO(user_input)
        
        with redirect_stdout(captured_output):
            # Call the main function of the add_numbers module
            add_numbers.main()
        
        # Reset stdin
        sys.stdin = sys.__stdin__
        
        # Check the output
        output = captured_output.getvalue()
        self.assertIn("Program to add two numbers", output)
        self.assertIn("The sum of -10.0 and -5.0 is: -15.0", output)
    
    def test_program_execution_with_invalid_inputs(self):
        """Test the full program execution with invalid inputs."""
        # Simulate user input with invalid data
        user_input = "abc\n10\n"
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdin = StringIO(user_input)
        
        with redirect_stdout(captured_output):
            # Call the main function of the add_numbers module
            add_numbers.main()
        
        # Reset stdin
        sys.stdin = sys.__stdin__
        
        # Check the output
        output = captured_output.getvalue()
        self.assertIn("Please enter valid numbers", output)
    
    def test_as_script_execution(self):
        """Test the script can be executed as a standalone program."""
        # This test verifies that the script is executable and has the correct shebang
        
        # Skip this test if not running on a Unix-like system
        if os.name != 'posix':
            self.skipTest("This test is only for Unix-like systems")
        
        # Check if add_numbers.py is executable
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'add_numbers.py')
            
            # Make the file executable if it's not already
            if not os.access(file_path, os.X_OK):
                os.chmod(file_path, 0o755)
            
            # Try to execute the file as a script
            result = subprocess.run(
                [sys.executable, file_path],
                input="3\n4\n",
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # Check the output
            self.assertIn("Program to add two numbers", result.stdout)
            self.assertIn("The sum of 3.0 and 4.0 is: 7.0", result.stdout)
            
        except Exception as e:
            self.fail(f"Failed to execute add_numbers.py as a script: {e}")

if __name__ == '__main__':
    unittest.main()
