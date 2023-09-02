"""
1171. Remove Zero Sum Consecutive Nodes from Linked List
========================================================
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no
such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
----------
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
----------
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
----------
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
------------
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n).
    Space complexity: O(n).
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        current_node = head

        prefix_sum_map = {}
        prefix_sum = 0
        while current_node:
            prefix_sum += current_node.val
            if prefix_sum in prefix_sum_map:
                prefix_sum_map[prefix_sum].next = current_node.next
                prefix_sum_map = {}
                prefix_sum = 0
                current_node = head
            else:
                prefix_sum_map[prefix_sum] = current_node
                current_node = current_node.next

        return head.next
