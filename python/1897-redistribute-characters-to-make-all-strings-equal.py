"""
1897. Redistribute Characters to Make All Strings Equal
=======================================================
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from
words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:
----------
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
----------
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:
------------
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    """
    Algorithm
    ---------
    Let's say that the length of words is len_words. If a given letter has a frequency of freq, we need to allocate
    freq / len_words copies to each string. This is only possible if freq / len_words is an integer, i.e.
    freq is divisible by len_words. We can check if freq is divisible by len_words by taking the modulus.
    If freq % len_words = 0, then freq is divisible by len_words.

    Complexity analysis
    -------------------
    Time complexity: O(n*k). Where n is the length of words and k is the average length of the elements in words.
    Space complexity: O(1)
    """

    def makeEqual(self, words: List[str]) -> bool:
        word_amount = len(words)

        counter = {}
        for word in words:
            for char in word:
                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1

        for frequency in counter.values():
            if frequency % word_amount != 0:
                return False

        return True
