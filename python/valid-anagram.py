class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not len(s) == len(t):
            return False

        d1 = {}
        d2 = {}

        for idx in range(len(s)):
            if s[idx] in d1:
                d1[s[idx]] += 1
            else:
                d1[s[idx]] = 1

            if t[idx] in d2:
                d2[t[idx]] += 1
            else:
                d2[t[idx]] = 1

        if d1 == d2:
            return True

        return False
