from collections import defaultdict

"""
1657. Determine if Two Strings Are Close
========================================

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, "abcde" -> "aecdb"
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with 
the other character.
For example, "aacabb" -> "bbcbaa" (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
----------
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
----------
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
----------
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
------------
1 <= word1.length, word2.length <= 10**5
word1 and word2 contain only lowercase English letters.
"""


class Solution:
    """
    Two strings are close if they have equal amount of:
    1) Letters;
    2) Occurrences of letters.

    Time complexity O(n)
    Space complexity O(1)
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = defaultdict(lambda: 0)
        d2 = defaultdict(lambda: 0)

        for l in word1:
            d1[l] += 1

        for l in word2:
            d2[l] += 1

        if sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(d2.values()):
            return True

        return False
