"""
1456. Maximum Number of Vowels in a Substring of Given Length
=============================================================

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
----------
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
----------
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
----------
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
------------
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    """
    Algorithm
    ---------
    Count vowels in the window.
    Update max_count.

    Iterate until right reaches the end of the string.
        Shift window by 1.
        If the left-1 element was a vowel, decrement count.
        If the right element is a vowel, increment count
        Update max_count in count > max_count.

    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def maxVowels(self, s: str, k: int) -> int:
        last_idx = len(s) - 1
        count = 0
        for i in range(k):
            if s[i] in self.VOWELS:
                count += 1

        max_count = count

        left_ptr = 0
        right_ptr = k
        while right_ptr <= last_idx:
            if s[left_ptr] in self.VOWELS:
                count -= 1

            if s[right_ptr] in self.VOWELS:
                count += 1
            left_ptr += 1
            right_ptr += 1

            if count >= max_count:
                max_count = count

        return max_count
