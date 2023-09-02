"""
1160. Find Words That Can Be Formed by Characters
=================================================
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
----------
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
----------
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
------------
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""
from collections import Counter
from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Given n as the length of chars, m as the length of words and k as the average length of each word in words,

    Time complexity: O(n+m*k)
    Space complexity: O(1). We use extra space for counts and wordCount. However, the input only contains lowercase
    English letters. Thus, the size of these hash maps never exceed 26, so we use O(1) space.
    """

    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        lengths = 0

        for word in words:
            all_there = True

            word_char_counter = Counter(word)
            for char in word_char_counter:
                if not (char in chars_counter and word_char_counter[char] <= chars_counter[char]):
                    all_there = False
                    break

            if all_there:
                lengths += len(word)

        return lengths
