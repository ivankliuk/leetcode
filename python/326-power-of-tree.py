"""
326. Power of Three
===================
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.


Example 1:
----------
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
----------
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
----------
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).

Constraints:
------------
-2^31 <= n <= 2^31 - 1
"""


class Solution:
    """
    Algorithm
    ---------
    Time complexity O(log n)
    Space complexity O(1)
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
