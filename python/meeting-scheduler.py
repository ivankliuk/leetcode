from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        idx1 = idx2 = 0

        slots1 = sorted(slots1)
        slots2 = sorted(slots2)

        while idx1 <= len(slots1) - 1 and idx2 <= len(slots2) - 1:
            s1 = slots1[idx1]
            s2 = slots2[idx2]
            left_intersection = max(s1[0], s2[0])
            right_intersection = min(s1[1], s2[1])
            if right_intersection - left_intersection >= duration:
                return [left_intersection, left_intersection + duration]

            # always move the one that ends earlier!
            if s1[1] < s2[1]:
                idx1 += 1
            else:
                idx2 += 1

        return []
