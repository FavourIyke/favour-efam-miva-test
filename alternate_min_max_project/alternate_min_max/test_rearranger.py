# tests/test_rearranger.py

import unittest
from rearranger import rearrange

class TestRearranger(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(rearrange([13, 7, 8, 3, 2, 10, 15, -1]), [-1, 15, 2, 13, 3, 10, 7, 8])
        self.assertEqual(rearrange([-5, -12, -1, 7, 14, -7, 3, 6]), [-12, 14, -7, 7, -5, 6, -1, 3])
        self.assertEqual(rearrange([3, 6, 9, -10, -5, -2, 0, 8]), [-10, 9, -5, 8, -2, 6, 0, 3])

    def test_edge_cases(self):
        self.assertEqual(rearrange([]), [])
        self.assertEqual(rearrange([42]), [42])
        self.assertEqual(rearrange([2, 1]), [1, 2])
        self.assertEqual(rearrange([5, 3, 4]), [3, 5, 4])

if __name__ == "__main__":
    unittest.main()
