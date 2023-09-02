from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        last_idx = len(arr) - 1

        while i < last_idx and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == last_idx:
            return False

        while i < last_idx and arr[i] > arr[i + 1]:
            i += 1

        if i != last_idx:
            return False

        return True
