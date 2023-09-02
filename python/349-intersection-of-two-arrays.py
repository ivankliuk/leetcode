"""
349. Intersection of Two Arrays
===============================
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
----------
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
----------
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
------------
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n+m) in the average case and O(n*m) in the worst case when the load factor is high enough.
    Space complexity: O(n+m) in the worst case when all elements in the arrays are different.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n*log(n) + m*log(m)), where nnn and mmm are the arrays' lengths.
    Space complexity: O(n+m) in the worst case when all elements in the arrays are different.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        common = []
        i = j = 0
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] == nums2[j]:
                if not (common and common[-1] == nums1[i]):
                    common.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return common
