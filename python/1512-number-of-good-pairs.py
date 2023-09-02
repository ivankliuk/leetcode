from typing import List

"""
1512. Number of Good Pairs
==========================
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
----------
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
----------
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
----------
Input: nums = [1,2,3]
Output: 0

Constraints:
------------
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    """
    Algorithm
    ---------
    Count all occurrences of a number.
    Number of pairs is a sum of arithmetical progression n * (n - 1) // 2.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = {}
        pair_count = 0

        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        for num in table:
            pair_count += table[num] * (table[num] - 1) // 2

        return pair_count
