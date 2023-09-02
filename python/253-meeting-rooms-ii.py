"""
253. Meeting Rooms II
=====================
Given an array of meeting time intervals  where intervals[i] = [start_i, end_i], return the minimum number
of conference rooms required.


Example 1:
----------
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
----------
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
------------
1 <= intervals.length <= 10^4
0 <= start_i < end_i <= 10^6
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n * log(n)).
    Space complexity: O(n). Because sorting in place takes additional space.
    """

    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            begins = sorted([t[0] for t in intervals])
            ends = sorted([t[1] for t in intervals])

            last_idx = len(intervals) - 1
            max_count = count = 0
            i = j = 0
            while i <= last_idx and j <= last_idx:
                if begins[i] < ends[j]:
                    i += 1
                    count += 1
                else:
                    j += 1
                    count -= 1
                max_count = max(max_count, count)

            return max_count
