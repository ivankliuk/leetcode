from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_seq = longest_seq = 0

        for num in nums:
            if num == 1:
                current_seq += 1

                if current_seq > longest_seq:
                    longest_seq = current_seq
            else:
                current_seq = 0

        return longest_seq
