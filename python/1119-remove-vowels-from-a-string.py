"""
1119. Remove Vowels from a String
=================================
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
----------
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
----------
Input: s = "aeiou"
Output: ""

Constraints:
------------
1 <= s.length <= 1000
s consists of only lowercase English letters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(1).
    """
    VOWELS = set("aeiou")

    def removeVowels(self, s: str) -> str:
        result = []
        for char in s:
            if char not in self.VOWELS:
                result.append(char)

        return "".join(result)
