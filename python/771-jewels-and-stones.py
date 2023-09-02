"""
771. Jewels and Stones
======================
You're given strings jewels representing the types of stones that are jewels, and stones representing 
the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones 
you have are also jewels.

Letters are case-sensitive, so "a" is considered a different type of stone from "A".

Example 1:
----------
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
----------
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
------------
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time Complexity: O(J.length+S.length).
    The O(J.length) part comes from creating J. The (S.length) part comes from searching S.

    Space Complexity: O(J.length).
    """

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)

        amount = 0
        for stone in stones:
            if stone in jewels_set:
                amount += 1

        return amount
