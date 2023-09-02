"""
1614. Maximum Nesting Depth of the Parentheses
==============================================
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

 * It is an empty string "", or a single character not equal to "(" or ")",
 * It can be written as AB (A concatenated with B), where A and B are VPS's, or
 * It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

 * depth("") = 0
 * depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
 * depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
 * depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

Example 1:
----------
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
----------
Input: s = "(1)+((2))+(((3)))"
Output: 3
"""


class Solution:
    """
    Algorithm
    ---------
    The depth of any character in the VPS is the (number of left brackets before it) - (number of right brackets before it)

    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(1).
    """

    def maxDepth(self, s: str) -> int:
        if len(s) == 1:
            return 0

        stack_l = 0
        stack_r = 0
        max_nesting = 0

        for char in s:
            if char == "(":
                stack_l += 1
            elif char == ")":
                stack_r += 1
            max_nesting = max(max_nesting, stack_l - stack_r)

        return max_nesting


class Solution1:
    def maxDepth(self, s: str) -> int:
        if len(s) == 1:
            return 0

        counter = 0
        max_nesting = 0

        for char in s:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
            max_nesting = max(max_nesting, counter)

        return max_nesting


class Solution2:
    """
    Algorithm
    ---------
    The maximum nesting depth is equal to the maximum number of open brackets at a time.

    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def maxDepth(self, s: str) -> int:
        if len(s) == 1:
            return 0

        stack = []
        max_nesting = 0

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop(-1)
            max_nesting = max(max_nesting, len(stack))

        return max_nesting
