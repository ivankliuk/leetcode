from typing import List

def has_even_digits(num: int) -> bool:
    count = 0
    for power in range(64):
        if num // 10 ** power != 0:
            count += 1
        else:
            break

    if count % 2 == 0:
        return True

    return False


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if has_even_digits(num):
                count += 1

        return count

