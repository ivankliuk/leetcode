"""
965. Univalued Binary Tree
==========================
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
----------
Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:
----------
Input: root = [2,2,2,5,2]
Output: false

Constraints:
------------
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n).
    Space complexity: O(n).
    """

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if node.val != value:
                    return False
                stack.append(node.left)
                stack.append(node.right)

        return True
