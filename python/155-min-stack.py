"""
155. Min Stack
==============
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
----------
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
------------
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class ListNode:
    def __init__(self, value, min_value, next_=None):
        self.value = value
        self.min_value = min_value
        self.next = next_


class MinStack:
    """
    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def __init__(self):
        self._ll = None

    def push(self, val: int) -> None:
        if self._ll:
            self._ll = ListNode(val, min(val, self._ll.min_value), next_=self._ll)
        else:
            self._ll = ListNode(val, val)

    def pop(self) -> None:
        self._ll = self._ll.next
        if self._ll and self._ll.next:
            self._ll.min_value = min(self._ll.min_value, self._ll.next.min_value)

    def top(self) -> int:
        return self._ll.value

    def getMin(self) -> int:
        return self._ll.min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
