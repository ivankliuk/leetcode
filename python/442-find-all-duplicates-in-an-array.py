"""
442. Find All Duplicates in an Array
====================================
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears
once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
----------
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
----------
Input: nums = [1,1,2]
Output: [1]

Example 3:
----------
Input: nums = [1]
Output: []

Constraints:
------------
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1

        result = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                result.append(abs(num))
                nums[abs(num) - 1] *= -1

        return result
