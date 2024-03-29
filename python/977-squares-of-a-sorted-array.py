"""
977. Squares of a Sorted Array
==============================
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted 
in non-decreasing order.

Example 1:
----------
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
----------
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
------------
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_sq = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        ptr = len(nums) - 1

        while ptr >= 0:
            if i == j:
                sorted_sq[ptr] = nums[j] ** 2
            elif nums[i] ** 2 > nums[j] ** 2:
                sorted_sq[ptr] = nums[i] ** 2
                i += 1
            else:
                sorted_sq[ptr] = nums[j] ** 2
                j -= 1
            ptr -= 1

        return sorted_sq
