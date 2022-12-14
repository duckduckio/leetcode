import unittest

from src.length_of_longest_substring import Solution


class Test(unittest.TestCase):

    def test_length_of_longest_substring(self):
        self.assertEqual(0, Solution().lengthOfLongestSubstring(None))
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, Solution().lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(7, Solution().lengthOfLongestSubstring("abcdabefg"))
