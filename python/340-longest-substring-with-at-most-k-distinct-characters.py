"""
340. Longest Substring with At Most K Distinct Characters
=========================================================
Given a string s and an integer k, return the length of the longest
substring of s that contains at most k distinct characters.

Example 1:
----------
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
----------
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:
------------
1 <= s.length <= 5 * 10^4
0 <= k <= 50
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(k). Because, the size of this dictionary can be at most k elements.
    """

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = max_length = 0
        window = {}

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            while len(window) > k:
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
