"""
1920. Build Array from Permutation
==================================

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where 
ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Example 1:
----------
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]

Example 2:
----------
Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
 
Constraints:
------------
1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.
"""
from typing import List


class Solution:
    """
    Algorithm
    ---------
    [0, 2,    1,    5,    3,    4   ]
    [0, 2000, 1000, 5000, 3000, 4000]
    [0, 2001, 1002, 5004, 3005, 4003]
    [0,    1,    2,    4,    5,    3]

    Time complexity: O(n).
    Space complexity: O(1).
    """

    SHIFT_CONSTANT = 1000

    def buildArray(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            nums[idx] *= self.SHIFT_CONSTANT

        for idx in range(len(nums)):
            extracted_idx = nums[idx] // self.SHIFT_CONSTANT
            nums[idx] = nums[idx] + nums[extracted_idx] // self.SHIFT_CONSTANT

        for idx in range(len(nums)):
            nums[idx] = nums[idx] % self.SHIFT_CONSTANT

        return nums
