from typing import List


class Solution:
    def count(self, n: int):
        sum = 0
        while n != 0:
            if n % 2 == 1:
                sum += 1
            n //= 2

        return sum

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count_i = self.count(i)
            result.append(count_i)

        return result
