from typing import List

"""
448. Find All Numbers Disappeared in an Array
=============================================
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
----------
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
----------
Input: nums = [1,1]
Output: [2]

Constraints:
------------
n == nums.length
1 <= n <= 10**5
1 <= nums[i] <= n
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(N)
    Space complexity: O(N)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_nums = set(range(1, len(nums) + 1))
        for num in nums:
            if num in missing_nums:
                missing_nums.remove(num)

        return list(missing_nums)


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(N)
    Space complexity: O(1)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            new_idx = abs(nums[idx]) - 1
            if nums[new_idx] > 0:
                nums[new_idx] *= -1

        missing_nums = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                missing_nums.append(idx + 1)

        return missing_nums
