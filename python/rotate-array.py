from typing import List


class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> List[int]:
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Algorithm:
        Rotate all            [7,6,5,4,3,2,1]
        Rotate from 0 to k-1  [5,6,7,4,3,2,1]
        Rotate from l to last [5,6,7,1,2,3,4]
        """
        if len(nums) < 2:
            return

        k %= len(nums)

        last_elem_idx = len(nums) - 1
        self.reverse(nums, 0, last_elem_idx)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, last_elem_idx)
