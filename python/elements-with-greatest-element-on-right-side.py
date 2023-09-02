from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_idx = len(arr) - 1
        max_value = arr[last_idx]
        arr[last_idx] = -1

        i = last_idx - 1

        while i >= 0:
            current_value = arr[i]
            arr[i] = max_value

            if current_value >= max_value:
                max_value = current_value

            i -= 1

        return arr
