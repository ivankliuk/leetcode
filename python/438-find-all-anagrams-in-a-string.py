from typing import List

"""
438. Find All Anagrams in a String
==================================
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
----------
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
----------
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
------------
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        p_dict = {}

        for char in p:
            if char in p_dict:
                p_dict[char] += 1
            else:
                p_dict[char] = 1

        window = {}
        for char in s[:len(p) - 1]:
            if char in window:
                window[char] += 1
            else:
                window[char] = 1

        l = 0
        r = len(p) - 1

        while r <= len(s) - 1:

            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            if window == p_dict:
                indices.append(l)

            if s[l] in window and window[s[l]] > 1:
                window[s[l]] -= 1
            else:
                del window[s[l]]

            l += 1
            r += 1

        return indices
