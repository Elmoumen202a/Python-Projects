import unittest
import os
from main import say_hello

class TestMain(unittest.TestCase):

    def test_say_hello_from_main_folder(self):
        # Set the current directory to the main folder of the project
        current_dir = os.path.dirname(os.path.abspath(__file__))
        main_dir = os.path.dirname(current_dir)
        os.chdir(main_dir)
        
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            
            # Call say_hello function
            say_hello()
            
            # Get the printed output
            output = out.getvalue().strip()
            
            # Assert that "Hello!" is printed
            self.assertEqual(output, "Hello!")
        finally:
            sys.stdout = saved_stdout

    def test_say_hello_from_different_folder(self):
        # Set the current directory to a different folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_dir)
        
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            
            # Call say_hello function
            say_hello()
            
            # Get the printed output
            output = out.getvalue().strip()
            
            # Assert that "This is not your folder." is printed
            self.assertEqual(output, "This is not your folder.")
        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()
