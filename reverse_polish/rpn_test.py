import unittest

import rpn

class RPN(unittest.TestCase):
    def test_calculate_with_one_operand(self):
        self.assertEqual(rpn.calculate('3 4 +'), 7)


    def test_calculate_with_many_operand(self):
        self.assertEqual(rpn.calculate('15 7 1 1 + - / 3 * 2 1 1 + + -'), 5)

if __name__ == '__main__':
    unittest.main()
