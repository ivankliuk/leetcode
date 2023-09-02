"""
11. Container With Most Water
=============================
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of t
he ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
----------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
----------
Input: height = [1,1]
Output: 1

Constraints:
------------
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Algorithm
        ---------
        Two pointers: left in the beginning, right in the end.
        Calculate area and update max_area if needed.
        If right height is greater than left height, increment left pointer and vise versa.
        Continue until two pointers meet.

        Complexity Analysis
        -------------------
        Time complexity: O(N)
        Space complexity: O(1)
        """

        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = (j - i) * min(height[j], height[i])

            if area > max_area:
                max_area = area

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return max_area
