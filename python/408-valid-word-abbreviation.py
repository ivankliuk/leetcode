"""
408. Valid Word Abbreviation
============================
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):
 - "s10n" ("s ubstitutio n")
 - "sub4u4" ("sub stit u tion")
 - "12" ("substitution")
 - "su3i1u2on" ("su bst i t u ti on")
 - "substitution" (no substrings replaced)

The following are not valid abbreviations:
 - "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
 - "s010n" (has leading zeros)
 - "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
----------
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

Example 2:
----------
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

Constraints:
------------
1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(n)
    """

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        s_abbr = []

        while i <= len(abbr) - 1:
            if abbr[i].isnumeric() and len(s_abbr) > 0 and s_abbr[-1].isnumeric():
                s_abbr[-1] += abbr[i]
            else:
                s_abbr.append(abbr[i])
            i += 1

        i = 0
        j = 0
        while i <= len(word) - 1 and j <= len(s_abbr) - 1:
            if s_abbr[j].isalpha():
                if s_abbr[j] == word[i]:
                    i += 1
                else:
                    return False
            else:
                if s_abbr[j].startswith("0"):
                    return False

                i += int(s_abbr[j])

            j += 1

        # Both of the pointers reached the end of the corresponding arrays
        if i != len(word) or j != len(s_abbr):
            return False

        return True
