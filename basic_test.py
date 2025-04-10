# test_basic_script.py
import unittest
from basic import add_numbers, subtract_numbers

class TestBasicScript(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(3, 5), -2)

if __name__ == '__main__':
    unittest.main()