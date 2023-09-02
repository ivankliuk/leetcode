"""
57. Insert Interval
===================
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent the start
and the end of the ith interval and intervals is sorted in ascend_ing order by start_i.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascend_ing order by start_i and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.


Example 1:
----------
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
----------
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
------------
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^5
intervals is sorted by start_i in ascend_ing order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""
from typing import List


class Solution:
    """
    Algorithm
    ---------
    1. Add non-overlapping intervals before facing overlapping.
    2. Merge overlapping intervals if any.
    3. Add non-overlapping intervals after facing overlapping.

    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        last_idx = len(intervals) - 1
        new_intervals = []
        i = 0

        while i <= last_idx:
            if intervals[i][1] < newInterval[0]:
                new_intervals.append(intervals[i])
                i += 1
            else:
                break

        while i <= last_idx:
            #                intervals[0][i]                intervals[1][i]
            # newInterval[0]                 newInterval[1]
            if (intervals[i][0] <= newInterval[1] <= intervals[i][1]

            # intervals[0][i]                intervals[1][i]
            #                 newInterval[0]                 newInterval[1]
            ) or (intervals[i][0] <= newInterval[0] <= intervals[i][1]

            # intervals[0][i]                               intervals[1][i]
            #                 newInterval[0] newInterval[1]
            ) or (intervals[i][0] <= newInterval[0] and newInterval[1] <= intervals[i][1]

            #                intervals[0][i] intervals[1][i]
            # newInterval[0]                                 newInterval[1]
            ) or (newInterval[0] <= intervals[i][0] and intervals[i][1] <= newInterval[1]):
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
            else:
                break

        new_intervals.append(newInterval)

        while i <= last_idx:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals


class Solution1:
    """
    Optimized solution using a single if-clause for determining overlapping intervals.
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        last_idx = len(intervals) - 1
        new_intervals = []
        i = 0

        while i <= last_idx and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1

        while i <= last_idx and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        new_intervals.append(newInterval)

        while i <= last_idx:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals
