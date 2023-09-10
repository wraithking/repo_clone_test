import unittest
from Calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
