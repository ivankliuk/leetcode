"""
387. First Unique Character in a String
=======================================

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
----------
Input: s = "leetcode"
Output: 0

Example 2:
----------
Input: s = "loveleetcode"
Output: 2

Example 3:
----------
Input: s = "aabb"
Output: -1

Constraints:
------------
1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(N) since we go through the string of length N two times.
    Space complexity: O(1) because English alphabet contains 26 letters.
    """

    def firstUniqChar(self, s: str) -> int:
        tracker = {}

        for char in s:
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1

        for idx, char in enumerate(s):
            if tracker[char] == 1:
                return idx

        return -1
