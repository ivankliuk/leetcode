"""
36. Valid Sudoku
================
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
----------
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
----------
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
------------
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n*n)
    Space complexity: O(n*n)
    """

    def is_valid_list(self, lst: List[str]):
        count_elements = 0
        nums = set()

        for n in lst:
            if not n == ".":
                nums.add(int(n))
                count_elements += 1

        return len(nums) == count_elements

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lines = board
        boxes = {}

        for i in range(9):
            row = []
            for j in range(9):
                key = i // 3 * 10 + j // 3
                if key in boxes:
                    boxes[key].append(board[i][j])
                else:
                    boxes[key] = [board[i][j]]
                row.append(board[j][i])

            if not self.is_valid_list(lines[i]) or not self.is_valid_list(row):
                return False

        for l in boxes.values():
            if not self.is_valid_list(l):
                return False

        return True
