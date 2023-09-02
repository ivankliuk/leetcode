"""
143. Reorder List
=================
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
----------
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
----------
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
------------
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
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
    Time complexity O(n).
    Space complexity O(1).
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head

        # 1. Find a middle node of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Cut the list in the middle
        curr = head
        while curr.next != slow:
            curr = curr.next
        curr.next = None

        # 3. Reverse the second part of the list
        prev = ListNode(slow.val)
        curr = slow.next
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        # 4. Merge two lists
        curr1 = head
        curr2 = prev
        curr_head = ListNode()
        while curr1 and curr2:
            curr_head.next = curr1
            curr_head = curr_head.next
            curr1 = curr1.next
            curr_head.next = curr2
            curr_head = curr_head.next
            curr2 = curr2.next
