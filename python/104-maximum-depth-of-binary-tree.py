"""
104. Maximum Depth of Binary Tree
=================================
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to
the farthest leaf node.

Example 1:
----------
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
----------
Input: root = [1,null,2]
Output: 2

Constraints:
------------
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        stack = [(1, root)]

        while stack:
            curr_depth, node = stack.pop()

            max_depth = max(curr_depth, max_depth)
            if node.left:
                stack.append((curr_depth + 1, node.left))
            if node.right:
                stack.append((curr_depth + 1, node.right))

        return max_depth


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n).
    Space complexity: O(n).
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        root.val = 1
        stack = [root]

        while stack:
            node = stack.pop()
            curr_depth = node.val
            max_depth = max(curr_depth, max_depth)
            if node.left:
                node.left.val = curr_depth + 1
                stack.append(node.left)
            if node.right:
                node.right.val = curr_depth + 1
                stack.append(node.right)

        return max_depth
