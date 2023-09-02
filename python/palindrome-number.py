from typing import List


def is_met(digits: List[int]) -> bool:
    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1

    return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        i = x
        while i:
            remainder = i % 10
            digits.append(remainder)
            i //= 10

        return is_met(digits)
