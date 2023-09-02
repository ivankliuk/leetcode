"""
1134. Armstrong Number
======================
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

Example 1:
----------
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:
----------
Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

Constraints:
------------
1 <= n <= 10^8
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isArmstrong(self, n: int) -> bool:
        num = 0
        str_n = str(n)

        for digit in str_n:
            num += int(digit) ** len(str_n)

        return num == n


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity : O(m), where `m` is the number of digits in integer `n`.
    Space complexity : O(1)
    """

    def isArmstrong(self, n: int) -> bool:
        digits_count = 0
        nn = n
        while nn != 0:
            nn //= 10
            digits_count += 1

        num = 0
        left = n
        while left != 0:
            left, right = left // 10, left % 10
            num += right ** digits_count

        return num == n
