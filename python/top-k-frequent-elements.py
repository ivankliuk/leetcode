from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        result = list(map(lambda a: a[0], sorted(d.items(), key=lambda a: a[1], reverse=True)[:k]))

        return result
