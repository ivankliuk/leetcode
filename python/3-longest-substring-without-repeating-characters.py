"""
3. Longest Substring Without Repeating Characters
=================================================
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
----------
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
----------
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
----------
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
------------
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
            else:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
                l += 1

            longest = max(r - l + 1, longest)

        return longest
