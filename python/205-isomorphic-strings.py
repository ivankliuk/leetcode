"""
205. Isomorphic Strings
=======================
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
----------
Input: s = "egg", t = "add"
Output: true

Example 2:
----------
Input: s = "foo", t = "bar"
Output: false

Example 3:
----------
Input: s = "paper", t = "title"
Output: true

Constraints:
------------
1 <= s.length <= 5 * 10**4
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n) since we go through the string of length `n` one time.
    Space complexity: O(1) because English alphabet contains 26 letters.
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_tracker = {}
        t_tracker = {}

        for idx in range(len(s)):
            if s[idx] in s_tracker:
                cur_list = s_tracker[s[idx]]
                cur_list.append(idx)
                s_tracker[s[idx]] = cur_list
            else:
                s_tracker[s[idx]] = [idx]

            if t[idx] in t_tracker:
                cur_list = t_tracker[t[idx]]
                cur_list.append(idx)
                t_tracker[t[idx]] = cur_list
            else:
                t_tracker[t[idx]] = [idx]

        return sorted(list(s_tracker.values())) == sorted(list(t_tracker.values()))


class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}

        for idx in range(len(s)):
            mapping_s[s[idx]] = t[idx]
            mapping_t[t[idx]] = s[idx]

        for idx in range(len(s)):
            if not (mapping_s[s[idx]] == t[idx] and mapping_t[t[idx]] == s[idx]):
                return False

        return True
