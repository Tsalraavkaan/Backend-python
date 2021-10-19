import unittest
from custom_list import CustomList


class TestList(unittest.TestCase):
    def setUp(self):
        self.lst = CustomList([1, 2, 3])

    def test_add(self):
        b = self.lst + [1, 2, -3]
        self.assertEqual(b, [2, 4, 0])

    def test_add2(self):
        b = [1, 2, 3, 4, 5] + self.lst
        self.assertEqual(b, [2, 4, 6, 4, 5])

    def test_sub(self):
        b = self.lst - [1, 2, -3]
        self.assertEqual(b, [0, 0, 6])

    def test_sub2(self):
        b = [1, 2, 3, 4, 5] - self.lst
        self.assertEqual(b, [0, 0, 0, 4, 5])

    def test_iadd_and_isub(self):
        b = CustomList(self.lst - [1, 2, -3])
        b += [1, 1, 1, 1, 1]
        b -= [1]
        self.assertEqual(b, [0, 1, 7, 1, 1])

    def test_comparisons(self):
        b = CustomList([0])
        c = CustomList([1, 1, 1, 1, 1, 1])
        d = CustomList([3, 3, 4])
        self.assertTrue(self.lst > b)
        self.assertTrue(self.lst >= c)
        self.assertTrue(self.lst == c)
        self.assertFalse(self.lst != c)
        self.assertTrue(self.lst < d)
        self.assertFalse(c <= b)


if __name__ == "__main__":
    unittest.main()
