from typing import List

"""
334. Increasing Triplet Subsequence
===================================
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and 
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
----------
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
----------
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
----------
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 
Constraints:
------------
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    """
    Algorithm
    ---------
    first_num = second_num = some very big number
    for n in nums:
        if n is smallest number:
            first_num = n
        else if n is second smallest number:
            second_num = n
        else n is bigger than both first_num and second_num:
            # We have found our triplet, return True

    # After loop has terminated
    # If we have reached this point, there is no increasing triplet, return False

    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(n)
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1

        if last_idx <= 1:
            return False

        nums_i = 2 ** 31 - 1
        nums_j = 2 ** 31 - 1

        # Three cases:
        # 1) n < nums_i < nums_j
        # 2) nums_i < n < nums_j
        # 3) nums_i < nums_j < n
        for n in nums:
            if n < nums_i and n < nums_j:
                nums_i = n
            elif nums_i < n < nums_j:
                nums_j = n
            elif nums_i < nums_j < n:
                return True

        return False
