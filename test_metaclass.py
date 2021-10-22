import unittest
from metaclass import CustomMeta


class CustomClass(metaclass=CustomMeta):

    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __add__(self, other):
        return self.custom_val + other.custom_val

    def not_magic_str__(self):
        return str(self.custom_val)


class TestList(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_default(self):
        """Default tests."""
        self.assertEqual(self.inst.custom_x, 50)
        self.assertEqual(self.inst.custom_line(), 100)
        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val
        with self.assertRaises(AttributeError):
            self.inst.line()
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_new_field(self):
        """New field test."""
        self.inst.y = 11
        self.assertEqual(self.inst.custom_y, 11)
        with self.assertRaises(AttributeError):
            self.inst.y

    def test_add(self):
        """Test magic methods."""
        obj = CustomClass(12)
        self.assertEqual(self.inst + obj, 111)

    def test_not_magic_methods(self):
        """Test not magic methods ended with "__"."""
        self.assertEqual(self.inst.custom_not_magic_str__(),
                         str(self.inst.custom_val))
        with self.assertRaises(AttributeError):
            self.assertEqual(self.inst.not_magic_str__(),
                             str(self.inst.custom_val))


if __name__ == "__main__":
    unittest.main()
