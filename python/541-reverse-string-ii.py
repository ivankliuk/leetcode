"""
541. Reverse String II
======================
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start
of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to
k characters, then reverse the first k characters and leave the other as original.


Example 1:
----------
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
----------
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:
------------
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(n)
    """

    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        idx = 0
        last_idx = len(s) - 1

        while idx <= last_idx:
            i = idx
            j = idx + k - 1

            if j > last_idx:
                j = last_idx

            while i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

            idx += 2 * k

        return "".join(s_list)
