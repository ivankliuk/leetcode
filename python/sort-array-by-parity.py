from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            current_value = nums[i]
            if nums[i] % 2 == 0:
                i += 1
            elif nums[i] % 2 != 0:
                while nums[j] % 2 != 0 and i < j:
                    j -= 1

                nums[i] = nums[j]
                nums[j] = current_value

        return nums


# Slower than previous
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0

        while i <= len(nums) - 1:
            current_value = nums[i]
            if nums[i] % 2 != 0:
                j = i
                while j <= len(nums) - 1:
                    if nums[j] % 2 == 0:
                        nums[i] = nums[j]
                        nums[j] = current_value
                        break
                    j += 1

                # we don't have even values after i-th element
                if j == len(nums) - 1:
                    return nums

            i += 1

        return nums