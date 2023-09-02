from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0
        last_idx = len(arr) - 1

        while i < last_idx:
            if arr[i] == 0:
                j = last_idx
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1

                arr[i + 1] = 0
                i += 2
            else:
                i += 1
