import unittest
from main import *
import nose


class TestCalculatorMethods(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(4, 3), 4 + 3)

    def test_sub(self):
        self.assertEquals(sub(4, 3), 4 - 3)

    def test_mul(self):
        self.assertEquals(mul(4, 3), 4 * 3)

    def test_div(self):
        self.assertEquals(div(4, 3), 4 / 3)


if __name__ == '__main__':
    unittest.main()
