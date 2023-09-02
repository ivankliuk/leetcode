"""
49. Group Anagrams
===================
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all 
the original letters exactly once.


Example 1:
----------
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
----------
Input: strs = [""]
Output: [[""]]

Example 3:
----------
Input: strs = ["a"]
Output: [["a"]]

Constraints:
------------
1 <= strs.length <= 10**4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Time Complexity: O(N*K*Log(K)), where N is the length of strs, and K is the maximum length of a string in strs.
    The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K*Log(K)) time.

    Space Complexity: O(N*K), the total information content stored in result.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = str(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        result = list(d.values())
        return result
