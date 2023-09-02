"""
21. Merge Two Sorted Lists
==========================
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
----------
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
----------
Input: list1 = [], list2 = []
Output: []

Example 3:
----------
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
------------
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
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
    Time complexity O(n + m). Where n and m are the lengths of list1 and list2 respectively.
    Space complexity O(n + m). Where n and m are the lengths of list1 and list2 respectively.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current_node = dummy_head
        while list1 or list2:
            if list1 is None:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
                current_node = current_node.next
            elif list2 is None:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
                current_node = current_node.next
            elif list1.val < list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
                current_node = current_node.next
            elif list1.val > list2.val:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
                current_node = current_node.next
            elif list1.val == list2.val:
                current_node.next = ListNode(list1.val, ListNode(list2.val))
                list1 = list1.next
                list2 = list2.next
                current_node = current_node.next.next

        return dummy_head.next


class Solution1:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n + m). Where n and m are the lengths of list1 and list2 respectively.
    Space complexity O(1)
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current_node = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1:
            current_node.next = list1
        elif list2:
            current_node.next = list2

        return dummy_head.next
