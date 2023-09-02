import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        last_idx = len(s) - 1

        ds = collections.defaultdict(lambda: 0)
        dt = collections.defaultdict(lambda: 0)

        while i <= last_idx:
            ds[s[i]] += 1
            dt[t[i]] += 1

            i += 1

        dt[t[-1]] += 1

        for key in dt:
            if key not in ds or ds[key] != dt[key]:
                return key
