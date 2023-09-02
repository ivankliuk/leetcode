"""
643. Maximum Average Subarray I
===============================
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any 
answer with a calculation error less than 10-5 will be accepted.

Example 1:
----------
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
----------
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
------------
n == nums.length
1 <= k <= n <= 10**5
-10**4 <= nums[i] <= 10**4
"""
from typing import List


class Solution:
    """
    Complexity analysis
    -------------------
    Time complexity : O(n)
    Space complexity : O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sliding_window = max_avg = sum(nums[:k])
        last_idx = len(nums) - 1

        start = 0
        end = start + k

        while end <= last_idx:
            sliding_window = sliding_window - nums[start] + nums[end]
            if sliding_window > max_avg:
                max_avg = sliding_window

            start += 1
            end += 1

        return max_avg / k
