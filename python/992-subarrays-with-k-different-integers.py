"""
992. Subarrays with K Different Integers
========================================
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
----------
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
----------
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
------------
1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(k). Because, the size of this dictionary can be at most k elements.
    """

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k - 1)

    def helper(self, nums: List[int], k: int) -> int:
        sub_arrays = 0
        l = 0
        window = {}

        for r in range(len(nums)):
            if nums[r] in window:
                window[nums[r]] += 1
            else:
                window[nums[r]] = 1

            while len(window) > k:
                if nums[l] in window:
                    window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1

            sub_arrays += r - l + 1

        return sub_arrays
