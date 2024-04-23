"""
1427. Perform String Shifts
===========================
You are given a string s containing lowercase English letters, and a matrix shift, where
shift[i] = [direction_i, amount_i]:
 - direction_i can be 0 (for left shift) or 1 (for right shift).
 - amount_i is the amount by which string s is to be shifted.
 - A left shift by 1 means remove the first character of s and append it to the end.
 - Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example 1:
----------
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
----------
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

Constraints:
------------
1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
direction_i is either 0 or 1.
0 <= amount_i <= 100
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for shift_step in shift:
            direction, amount = shift_step[0], shift_step[1] % len(s)
            if direction == 1:
                for _ in range(amount):
                    s = s[-1] + s[:-1]
            else:
                for _ in range(amount):
                    s = s[1:] + s[0]

        return s
