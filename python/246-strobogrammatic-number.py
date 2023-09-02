"""
246. Strobogrammatic Number
===========================
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).


Example 1:
----------
Input: num = "69"
Output: true

Example 2:
----------
Input: num = "88"
Output: true

Example 3:
----------
Input: num = "962"
Output: false

Constraints:
------------
1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    MAPPING = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    def isStrobogrammatic(self, num: str) -> bool:
        i = 0
        j = len(num) - 1

        while i <= j:
            if num[i] not in self.MAPPING or num[j] not in self.MAPPING:
                return False
            if num[i] == self.MAPPING[num[j]] or num[j] == self.MAPPING[num[i]]:
                i += 1
                j -= 1
            else:
                return False

        return True
