"""
2108. Find First Palindromic String in the Array
================================================
Given an array of strings words, return the first palindromic string in the array. If there is no such string, 
return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:
----------
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
----------
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
----------
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.

Constraints:
------------
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
"""

from typing import List


class Solution:
    """
    Complexity Analysis
    -------------------
    Let `n` be the number of strings in words and `m` be the maximum length of a string in it.

    Time complexity: O(nm). For each of the `n` strings in the list words, we iterate over each character once,
    and hence the time complexity is equal to O(nm).
    Space complexity: O(1).
    """

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i = 0
            j = len(word) - 1

            is_palindrome = True
            while i <= j and is_palindrome == True:
                if word[i] == word[j]:
                    i += 1
                    j -= 1
                else:
                    is_palindrome = False

            if is_palindrome:
                return word

        return ""
