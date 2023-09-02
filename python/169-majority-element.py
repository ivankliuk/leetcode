
"""
169. Majority Element
=====================
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.


Example 1:
----------
Input: nums = [3,2,3]
Output: 3

Example 2:
----------
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
------------
n == nums.length
1 <= n <= 5 * 10**4
-10**9 <= nums[i] <= 10**9
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_occurence = {}

        for num in nums:
            if num in num_occurence:
                num_occurence[num] += 1
            else:
                num_occurence[num] = 1

        maj = sorted(num_occurence.items(), key=lambda a: a[1])[-1][0]

        return maj


class Solution1:
    """
    Algorithm
    ---------
    Boyer–Moore majority vote algorithm.

    Time complexity O(n)
    Space complexity O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for num in nums[1:]:
            if num == candidate:
                count += 1
            elif count == 1:
                candidate = num
                count = 1
            else:
                count -= 1

        return candidate
