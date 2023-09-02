"""
28. Find the Index of the First Occurrence in a String
======================================================
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
----------
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
----------
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
------------
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(nm), where `n` and `m` are lengths of haystack and needle correspondingly.
    Space complexity: O(1)
    """

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        haystack_last_idx = len(haystack) - 1
        needle_last_idx = len(needle) - 1

        while i <= haystack_last_idx - needle_last_idx:
            if needle[0] == haystack[i]:
                j = 0
                while j <= needle_last_idx:
                    if needle[j] == haystack[j + i]:
                        j += 1
                    else:
                        break

                if j == needle_last_idx + 1:
                    return i

            i += 1

        return -1
