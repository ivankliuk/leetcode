"""
290. Word Pattern
=================
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
----------
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
----------
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
----------
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
------------
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity : O(N+M) where N represents the length of s and M represents the length of pattern.
    All operations in the algorithm are linear with the length of the inputs.

    Space complexity : O(W) where W represents the number of unique words in s. Even though we have two hash maps,
    the character to word hash map has space complexity of O(1) since there can at most be 26 keys.
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        patterns = [key for key in pattern]

        if len(strs) != len(patterns):
            return False

        mapping1 = {}
        mapping2 = {}
        for idx in range(len(strs)):
            if patterns[idx] in mapping2 and mapping2[patterns[idx]] != strs[idx]:
                return False
            else:
                mapping1[strs[idx]] = patterns[idx]
                mapping2[patterns[idx]] = strs[idx]

        if len(mapping2) != len(mapping1):
            return False

        return True


class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        patterns = [key for key in pattern]

        if len(strs) != len(patterns):
            return False

        mapping1 = {}
        mapping2 = {}

        for idx in range(len(strs)):
            if strs[idx] in mapping1 and mapping1[strs[idx]] != patterns[idx]:
                return False
            else:
                mapping1[strs[idx]] = patterns[idx]

            if patterns[idx] in mapping2 and mapping2[patterns[idx]] != strs[idx]:
                return False
            else:
                mapping2[patterns[idx]] = strs[idx]

        return True
