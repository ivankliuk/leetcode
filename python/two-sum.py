from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx in range(len(nums)):
            n1 = nums[idx]
            n2 = target - n1
            if n2 in d:
                return [idx, d[n2]]

            d[n1] = idx
