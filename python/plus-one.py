from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1

        while digits[idx] == 9:
            digits[idx] = 0
            idx -= 1

        # Last changed digit was 9 and idx is out of bound,
        # prepend 1 and return the result
        if idx == -1:
            return [1] + digits

        digits[idx] += 1
        return digits
