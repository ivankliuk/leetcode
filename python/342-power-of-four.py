"""
342. Power of Four
==================
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

Example 1:
----------
Input: n = 16
Output: true

Example 2:
----------
Input: n = 5
Output: false

Example 3:
----------
Input: n = 1
Output: true

Constraints:
------------
-2^31 <= n <= 2^31 - 1
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(log n)
    Space complexity O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1
