"""
2352. Equal Row and Column Pairs
================================
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
----------
Input: grid = [
    [3,2,1],
    [1,7,6],
    [2,7,7]
]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
----------
Input: grid = [
    [3,1,2,2],
    [1,4,4,5],
    [2,4,2,2],
    [2,4,2,2]
]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:
------------
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    Algorithm
    ---------
    1) Create an empty hash map row_counter and set count to 0.
    2) For each row in the grid, convert it into an equivalent hashable object and use it as a key to the row_counter.
       Increment the value of the corresponding key by 1.
    3) For each column in the grid, convert it into the same type of hashable object and check if it appears in
       the row_counter. If it does, increment count by the frequency.
    4) Return the answer count.

    Grid:      HashMap:
    [3,1,2,2]  (3,1,2,2) * 1
    [1,4,4,5]  (1,4,4,5) * 1
    [2,4,2,2]  (2,4,2,2) * 2
    [2,4,2,2]

    [3,1,2,2]  (3,1,2,2) * 1
    [1,4,4,5]  (1,4,4,5) * 1
    [2,4,2,2]  (2,4,2,2) * 2
    [2,4,2,2]
     ^

    Complexity analysis
    -------------------
    Time complexity O(n^2)
    Space complexity O(n^2)
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = defaultdict(lambda: 0)
        count = 0

        for i in range(len(grid)):
            row = [grid[i][j] for j in range(len(grid))]
            freq[tuple(row)] += 1

        for j in range(len(grid)):
            column = tuple([grid[i][j] for i in range(len(grid))])
            if column in freq:
                count += freq[column]

        return count
