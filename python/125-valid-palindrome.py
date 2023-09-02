"""
125. Valid Palindrome
=====================
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
----------
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
----------
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
----------
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
------------
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""


class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True
