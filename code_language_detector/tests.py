import unittest
from main import detect_language

class TestDetectLanguage(unittest.TestCase):
    def test_python(self):
        # Test case for Python code
        code = """
        def hello():
            print("Hello, World!")
        """
        self.assertEqual(detect_language(code), 'python')

    def test_java(self):
        # Test case for Java code
        code = """
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        """
        self.assertEqual(detect_language(code), 'java')

    def test_c(self):
        # Test case for C code
        code = """
        #include <stdio.h>
        int main() {
            printf("Hello, World!");
            return 0;
        }
        """
        self.assertEqual(detect_language(code), 'c')

    def test_cpp(self):
        # Test case for C++ code
        code = """
        #include <iostream>
        int main() {
            std::cout << "Hello, World!" << std::endl;
            return 0;
        }
        """
        self.assertEqual(detect_language(code), 'cpp')

    def test_unknown(self):
        # Test case for unknown language
        code = """
        print "Hello, World!"
        """
        self.assertEqual(detect_language(code), 'unknown')

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
