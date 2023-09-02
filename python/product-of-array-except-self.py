from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums   [1, 2, 3, 4, 5]

        l_nums [1, 1, 2, 6, 24]
        r_nums [120, 60, 20, 5, 1]

        result [120, 60, 40, 30, 24]
        """
        last_idx = len(nums) - 1

        l_nums = [0] * len(nums)
        r_nums = [0] * len(nums)

        i = 0
        while i <= last_idx:
            if i == 0:
                l_nums[i] = 1
            elif i == 1:
                l_nums[i] = nums[i - 1]
            else:
                l_nums[i] = nums[i - 1] * l_nums[i - 1]
            i += 1

        i = last_idx
        while i >= 0:
            if i == last_idx:
                r_nums[last_idx] = 1
            elif i == last_idx - 1:
                r_nums[i] = nums[i + 1]
            else:
                r_nums[i] = nums[i + 1] * r_nums[i + 1]
            i -= 1

        for i in range(len(nums)):
            nums[i] = l_nums[i] * r_nums[i]

        return nums
