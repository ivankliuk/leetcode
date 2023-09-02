"""
452. Minimum Number of Arrows to Burst Balloons
===============================================
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as 
a 2D integer array points where points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches
between x_start and x_end. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. There is no limit to
the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
----------
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
----------
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
----------
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
------------
1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= x_start < x_end <= 2^31 - 1
"""
from typing import List


class ListNode:
    def __init__(self, start, end, next_=None):
        self.start = start
        self.end = end
        self.next = next_


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n*log(n)).
    Space complexity: O(n).
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        head = ListNode(points[0][0], points[0][1])
        current_node = head

        for point in points[1:]:
            current_node.next = ListNode(point[0], point[1])
            current_node = current_node.next

        current_node = head
        counter = 1
        while current_node.next:
            if current_node.end >= current_node.next.start:
                current_node = ListNode(
                    max(current_node.start, current_node.next.start),
                    min(current_node.end, current_node.next.end),
                    current_node.next.next
                )
            else:
                current_node = current_node.next
                counter += 1

        return counter


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n*log(n)).
    Space complexity: O(n). Because sorting in place takes additional space.
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on the end coordinates
        points.sort(key=lambda x: x[0])

        # Initialize the counter and end coordinate with the first balloon's end coordinate
        counter = 1
        end = points[0][1]

        # Iterate through the points
        for start, new_end in points[1:]:
            # If the current balloon's start coordinate is greater than the previous end coordinate,
            # it means a new arrow is needed
            if start > end:
                counter += 1
                end = new_end  # Update the end coordinate

        return counter
