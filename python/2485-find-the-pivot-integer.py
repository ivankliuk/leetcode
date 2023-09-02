"""
2485. Find the Pivot Integer
============================
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one
pivot index for the given input.

Example 1:
----------
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
----------
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
----------
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:
------------
1 <= n <= 1000
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def pivotInteger(self, n: int) -> int:
        pivot_integer = -1
        left_sum = [0] * n
        left_sum[0] = 1

        idx = 1
        for num in range(2, n + 1):
            left_sum[idx] = left_sum[idx - 1] + num
            idx += 1

        right_sum = [0] * n
        right_sum[-1] = n
        num = n
        for idx in range(n - 2, -1, -1):
            num -= 1
            right_sum[idx] = right_sum[idx + 1] + num

        for idx in range(n):
            if left_sum[idx] == right_sum[idx]:
                return idx + 1

        return pivot_integer


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        prefix_sum_left = [0]

        for i in range(1, n):
            prefix_sum_left.append(prefix_sum_left[-1] + i)

        prefix_sum_right = n
        for i in range(n - 1, 0, -1):
            if prefix_sum_left[i - 1] == prefix_sum_right:
                return i
            prefix_sum_right += i
        return -1