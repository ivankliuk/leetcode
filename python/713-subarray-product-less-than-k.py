"""
713. Subarray Product Less Than K
=================================
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of
all the elements in the subarray is strictly less than k.

Example 1:
----------
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
----------
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
------------
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sub_arrays_count = 0
        if k <= 1:
            return sub_arrays_count

        r = 0
        l = 0
        window_product = 1

        while r <= len(nums) - 1:
            window_product *= nums[r]
            while window_product >= k and l <= len(nums) - 1:
                window_product //= nums[l]
                l += 1

            sub_arrays_count += r - l + 1
            r += 1

        return sub_arrays_count
