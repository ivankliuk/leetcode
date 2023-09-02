"""
697. Degree of an Array
=======================
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
----------
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
----------
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
------------
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from collections import Counter
from typing import List


class Solution:
    """
    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def findShortestSubArray(self, nums: List[int]) -> int:
        num_frequency = Counter(nums)
        degree = max(num_frequency.values())

        smallest_length = len(nums)
        for num, count in num_frequency.items():
            if count == degree:
                i = 0
                j = len(nums) - 1

                while nums[i] != num:
                    i += 1

                while nums[j] != num:
                    j -= 1

                smallest_length = min(smallest_length, j - i + 1)

        return smallest_length
