from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Algorithm:

        If number is not seen - add it to the hash table
        If number is seen - pop the element from the hash table
        Return the single element of the hash table
        """
        seen_nums = set()
        for num in nums:
            if num not in seen_nums:
                seen_nums.add(num)
            else:
                seen_nums.remove(num)

        return seen_nums.pop()
