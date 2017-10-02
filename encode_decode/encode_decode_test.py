import unittest

import encode_decode

class EncodeDecode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_decode.encode('eeeffffeee'), '3e4f2e')

    def test_encode_with_single_last_character(self):
        self.assertEqual(encode_decode.encode('eeeffffeee'), '3e4f2e')

    def test_decode(self):
        self.assertEqual(encode_decode.decode('2a3b1c'), 'aabbbc')

if __name__ == '__main__':
    unittest.main()
