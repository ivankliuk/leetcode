"""
202. Happy Number
=================
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
----------
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
----------
Input: n = 2
Output: false

Constraints:
------------
1 <= n <= 2^31 - 1
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(log(N))
    Space complexity O(log(n))
    """

    def _get_digit_square_sum(self, n: int) -> int:
        return sum(map(lambda x: int(x) ** 2, str(n)))

    def isHappy(self, n: int) -> bool:
        seen = set()
        digit_square_sum = n

        while digit_square_sum not in seen:
            seen.add(digit_square_sum)
            digit_square_sum = self._get_digit_square_sum(digit_square_sum)

        if digit_square_sum == 1:
            return True

        return False


class Solution1:
    def _get_digit_square_sum(self, n: int) -> int:
        square_sum = 0
        left = n
        while left > 0:
            left, right = left // 10, left % 10
            square_sum += right ** 2
        return square_sum

    def isHappy(self, n: int) -> bool:
        seen = set()
        digit_square_sum = n

        while digit_square_sum not in seen:
            seen.add(digit_square_sum)
            digit_square_sum = self._get_digit_square_sum(digit_square_sum)

        if digit_square_sum == 1:
            return True

        return False
