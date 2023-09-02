from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_sq = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        ptr = len(nums) - 1

        while ptr >= 0:
            if i == j:
                sorted_sq[ptr] = nums[j] ** 2
            elif nums[i] ** 2 > nums[j] ** 2:
                sorted_sq[ptr] = nums[i] ** 2
                i += 1
            else:
                sorted_sq[ptr] = nums[j] ** 2
                j -= 1
            ptr -= 1

        return sorted_sq
