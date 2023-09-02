from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(lambda: 0)

        for n in arr:
            d[n] += 1

        return len(d.keys()) == len(set(d.values()))
