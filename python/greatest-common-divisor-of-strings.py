class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        gcd = min(len1, len2)

        while gcd > 0:
            if len1 % gcd == 0 and len2 % gcd == 0:
                break
            gcd -= 1

        if gcd == 0:
            return ""

        common = str1[:gcd]

        if common * (len1 // gcd) == str1 and common * (len2 // gcd) == str2:
            return common

        return ""
py