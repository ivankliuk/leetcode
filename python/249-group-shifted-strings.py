from typing import List

"""
249. Group Shifted Strings
==========================
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Example 1:
----------
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
----------
Input: strings = ["a"]
Output: [["a"]]

Constraints:
------------
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    n - the length of strings
    k - the maximum length of a string in strings.

    Time complexity: O(n*k)
    Space complexity: O(n*k)
    """

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for word in strings:
            # Step 1: Get the first char of the word and use it as a starting point
            shift = ord(word[0])

            # Step 2: Represent all letters in the word as integer values and shift them
            pattern = [((ord(letter) - shift) % 26) for letter in word]

            key = tuple(pattern)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        result = list(groups.values())
        return result
