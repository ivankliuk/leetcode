from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = str(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        result = d.values()
        return result
