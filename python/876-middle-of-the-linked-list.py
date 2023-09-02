"""
876. Middle of the Linked List
==============================
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
----------

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
----------
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
------------
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        current_node = head
        length = 1
        while current_node.next:
            length += 1
            current_node = current_node.next

        middle = length // 2
        if middle == 0:
            middle += 1

        while middle != 0:
            middle -= 1
            head = head.next

        return head
