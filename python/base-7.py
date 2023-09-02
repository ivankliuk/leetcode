class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        l = abs(num)

        result = ""

        while l:
            result = str(l % 7) + result
            l //= 7

        if num < 0:
            result = "-" + result

        return result
