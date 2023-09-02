from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        seen_num_set = set()
        num_set = set(nums)

        if num_set:
            longest_seq = 1
        else:
            longest_seq = 0

        for num in num_set:
            if num in seen_num_set:
                continue
            current_seq = 1
            current_num = num

            while current_num + 1 in num_set:
                seen_num_set.add(current_num)
                current_num += 1
                current_seq += 1
                if longest_seq <= current_seq:
                    longest_seq = current_seq

        return longest_seq
