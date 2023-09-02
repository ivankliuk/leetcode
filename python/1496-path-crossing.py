"""
1496. Path Crossing
===================
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or
west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:
----------
Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
----------
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
------------
1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""


class Solution:
    """
    Complexity Analysis
    -------------------

    Time complexity: O(n). We iterate over each character of path once.
    Space complexity: O(n). When there are no crossings, visited will grow to a length of n.
    """

    def isPathCrossing(self, path: str) -> bool:
        point = (0, 0)
        points = {point}

        for step in path:
            if step == "N":
                point = point[0], point[1] + 1
            elif step == "S":
                point = point[0], point[1] - 1
            elif step == "W":
                point = point[0] - 1, point[1]
            elif step == "E":
                point = point[0] + 1, point[1]

            if point in points:
                return True

            points.add(point)

        return False
