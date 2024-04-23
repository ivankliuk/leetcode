"""
735. Asteroid Collision
=======================

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
----------
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
----------
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
----------
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
------------
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List


class Solution:
    """
    Complexity analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def _wrap_stack(self, stack: List[int]) -> List[int]:
        while len(stack) > 1 and stack[-2] > 0 > stack[-1]:
            if stack[-2] + stack[-1] == 0:
                stack.pop()
                stack.pop()
            elif abs(stack[-2]) < abs(stack[-1]):
                e = stack.pop()
                stack.pop()
                stack.append(e)
            else:
                stack.pop()

        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            stack.append(a)
            if a < 0:
                stack = self._wrap_stack(stack)

        return stack
