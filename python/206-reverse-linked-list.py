"""
206. Reverse Linked List
========================
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
----------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
----------
Input: head = [1,2]
Output: [2,1]

Example 3:
----------
Input: head = []
Output: []

Constraints:
------------
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        stack = []
        last_node = head

        while not last_node is None:
            stack.append(last_node.val)
            last_node = last_node.next

        new_head = ListNode(stack.pop())
        current = new_head
        for val in reversed(stack):
            current.next = ListNode(val)
            current = current.next

        return new_head


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n).
    Space complexity: O(n).
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head

        while current_node:
            if previous_node:
                previous_node = ListNode(current_node.val, previous_node)
            else:
                previous_node = ListNode(current_node.val)
            current_node = current_node.next

        return previous_node


class Solution3:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n).
    Space complexity: O(1).
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node
