"""
41. First Missing Positive
==========================
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
----------
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
----------
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
----------
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
------------
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    """
    Algorithm
    ---------
    Time complexity O(n)
    Space complexity O(n)
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        max_num = 0
        for num in nums:
            if num > 0:
                seen.add(num)
                if num > max_num:
                    max_num = num

        for num in range(1, max_num + 1):
            if num not in seen:
                return num
        return max_num + 1


class Solution1:
    """
    Algorithm
    ---------
    Time complexity O(n)
    Space complexity O(n)
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        smallest = 1

        for num in nums:
            if num > 0:
                if smallest < num:
                    seen.add(num)
                elif smallest == num:
                    smallest += 1
                    while smallest in seen:
                        smallest += 1

        return smallest
