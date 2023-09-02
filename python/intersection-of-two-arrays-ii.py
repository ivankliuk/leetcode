from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1_dict = {}
        nums2_dict = {}

        for num in nums1:
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1

        for num in nums2:
            if num in nums2_dict:
                nums2_dict[num] += 1
            else:
                nums2_dict[num] = 1

        for n in nums1_dict:
            if n in nums2_dict:
                if nums1_dict[n] < nums2_dict[n]:
                    intersection.extend([n] * nums1_dict[n])
                else:
                    intersection.extend([n] * nums2_dict[n])

        return intersection
