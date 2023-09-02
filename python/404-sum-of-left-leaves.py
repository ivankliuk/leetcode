"""
404. Sum of Left Leaves
=======================
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
----------
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
----------
Input: root = [1]
Output: 0

Constraints:
------------
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
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

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ll_sum = 0
        stack = [root]
        while stack:
            node = stack.pop()

            if node:
                if node.left and not node.left.left and not node.left.right:
                    ll_sum += node.left.val
                stack.append(node.left)
                stack.append(node.right)

        return ll_sum
