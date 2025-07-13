import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest

from Leetcode.trappingRainwater import Solution


class TestTrappingRainwater(unittest.TestCase):
    def test_example_case(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        self.assertEqual(Solution().trap(height), expected)


if __name__ == "__main__":
    unittest.main()
