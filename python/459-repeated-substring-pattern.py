"""
459. Repeated Substring Pattern
===============================
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies
of the substring together.


Example 1:
----------
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
----------
Input: s = "aba"
Output: false

Example 3:
----------
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
------------
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: ???.
    Space complexity: O(1).
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        for multiplier in filter(lambda x: len(s) % x == 0, range(1, len(s))):
            i = 0
            j = multiplier

            while j <= len(s) - 1:
                if s[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    break

            if j == len(s):
                return True

        return False
