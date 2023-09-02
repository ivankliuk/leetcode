
"""
219. Contains Duplicate II
==========================
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:
----------
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
----------
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
----------
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
------------
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
0 <= k <= 10**5
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n). We do n operations of search, delete and insert, each with constant time complexity.

    Space complexity: O(min(n,k)).
    The extra space required depends on the number of items stored in the hash table, which is the size of
    the sliding window, min(n,k).
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}

        for i, num in enumerate(nums):
            if num in window:
                j = window[num]
                if abs(i - j) <= k:
                    return True

            window[num] = i

        return False
