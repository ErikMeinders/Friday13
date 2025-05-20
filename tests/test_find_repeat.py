import unittest

from find_repeat import find_repeat


class FindRepeatTests(unittest.TestCase):
    """Tests for the :func:`find_repeat` utility."""

    def test_no_pattern(self):
        self.assertEqual(find_repeat([1, 2, 1, 2, 2, 3]), 0)
        self.assertEqual(find_repeat([1, 2, 1, 2, 1, 3]), 0)
        self.assertEqual(find_repeat([1, 2, 1, 2, 1, 2, 3]), 0)

    def test_detect_pattern(self):
        self.assertEqual(find_repeat([1, 2, 1, 2, 1, 2, 1]), 2)
        self.assertEqual(find_repeat([1, 2, 1, 2, 1, 2]), 2)
        self.assertEqual(find_repeat([1, 2, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2]), 5)
        self.assertEqual(find_repeat([1, 1, 1, 1]), 1)
        self.assertEqual(find_repeat([range(10)]), 0)


if __name__ == "__main__":
    unittest.main()
