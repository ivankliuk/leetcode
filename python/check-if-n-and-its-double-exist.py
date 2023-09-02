from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        [10,2,5,3]
        10 * 2 = 20 not in {}
         2 * 2 = 4  not in {10}
         5 * 2 = 10     in {10, 2} "a * 2 in seen"

        [7,1,14,11]
         7 * 2 = 14 not in {}
         1 * 2 = 2  not in {7}
        14 * 2 = 28 not in {7, 1} "a % 2 == 0 and a // 2 in seen"
        """
        seen = set()

        for a in arr:
            if a * 2 in seen or (a % 2 == 0 and a // 2 in seen):
                return True

            seen.add(a)

        return False
