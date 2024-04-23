"""
2444. Count Subarrays With Fixed Bounds
=======================================
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

* The minimum value in the subarray is equal to minK.
* The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:
----------
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
----------
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:
------------
2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(1).
    """

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_i = min_i = max_i = -1
        count = 0

        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                bad_i = i

            if nums[i] == minK:
                min_i = i

            if nums[i] == maxK:
                max_i = i

            count += max(0, min(min_i, max_i) - bad_i)

        return count
