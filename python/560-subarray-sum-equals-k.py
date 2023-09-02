"""
560. Subarray Sum Equals K
==========================
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
----------
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
----------
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
------------
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        idx = 1
        while idx <= len(nums):
            prefix_sum.append(prefix_sum[idx - 1] + nums[idx - 1])
            idx += 1

        sub_arrays = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                diff_sum = prefix_sum[j + 1] - prefix_sum[i]
                if diff_sum == k:
                    sub_arrays += 1

        return sub_arrays
