"""
3005. Count Elements With Maximum Frequency
===========================================
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Example 1:
----------
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
----------
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

Constraints:
------------
1 <= nums.length <= 100
1 <= nums[i] <= 100
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

    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_frequency = 0
        for count in counter.values():
            if count > max_frequency:
                max_frequency = count

        total_freq = 0
        for count in counter.values():
            if count == max_frequency:
                total_freq += count

        return total_freq


class Solution1:
    """
    Algorithm
    ---------
    One-pass traversing.

    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        max_frequency = 0
        total_freq = 0

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

            if counter[num] > max_frequency:
                max_frequency = counter[num]
                total_freq = 0

            if counter[num] == max_frequency:
                total_freq += max_frequency

        return total_freq
