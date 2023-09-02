class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0:
            if length > 0 and s[i] == " ":
                return length
            elif s[i] != " ":
                length += 1
            i -= 1

        return length
