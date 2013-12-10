import unittest

from color import Color

__author__ = 'Tyler Crompton'


class TestColorConstant(unittest.TestCase):
    def test(self):
        color = Color.GOLDENROD
        color.red = 255
        self.assertEqual(Color.GOLDENROD.red, 218)
        self.assertEqual(color.red, 255)
        Color.GOLDENROD.red = 255
        self.assertEqual(Color.GOLDENROD.red, 218)

if __name__ == '__main__':
    unittest.main()