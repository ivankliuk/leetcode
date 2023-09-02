class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0

        s_last_idx = len(s) - 1
        t_last_idx = len(t) - 1

        while s_ptr <= s_last_idx and t_ptr <= t_last_idx:
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

        if s_ptr == len(s):
            return True

        return False
