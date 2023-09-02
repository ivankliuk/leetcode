"""
557. Reverse Words in a String III
==================================
Given a string s, reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order.


Example 1:
----------
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
----------
Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:
------------
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n).
    Space complexity O(n).
    """

    def reverseWords(self, s: str) -> str:
        i = 0
        j = 0
        last_idx = len(s) - 1
        result = []

        while j <= last_idx:
            if s[j] != " " and j != last_idx:
                j += 1
            elif j == last_idx:
                c = j
                while c >= i:
                    result.append(s[c])
                    c -= 1
                j += 1
            else:
                c = j - 1
                while c >= i:
                    result.append(s[c])
                    c -= 1
                result.append(" ")
                j += 1
                i = j

        return "".join(result)
