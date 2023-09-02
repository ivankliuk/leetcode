from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = 0
        j = 1
        while j <= len(nums) - 1:
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            elif nums[i] == 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
            else:
                i += 1
                j += 1
