import unittest
from factorial import *


class TestFactorial(unittest.TestCase):

    def test_fact(self):
        """Any method method which ``test`` will considered as a test case."""
        result = fact(5)
        self.assertEqual(result, 120)

    def test_fact_with_large_number(self):
        result = fact(10)
        self.assertEqual(result, 3628800)

if __name__ == '__main__':
    unittest.main()
