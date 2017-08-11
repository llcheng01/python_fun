import unittest
from roman_numerals import numeral

class RomanNumeralsTestCase(unittest.TestCase):

    def test_four_shorten_successfully(self):
        """arabic number 4 shortened to IV based on shorten rule"""
        self.assertEqual(numeral(4), 'IV')

    def test_nine_shorten_successfully(self):
        """arabic number 9 shortened to IX based on shorten rule"""
        self.assertEqual(numeral(9), 'IX')

    def test_zeros_are_not_converted(self):
        for actual, expect in ([3000, 'MMM'], [1024, 'MXXIV']):
            self.assertEqual(numeral(actual), expect)

if __name__ == '__main__':
    unittest.main()
