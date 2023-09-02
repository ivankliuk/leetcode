class Solution:
    MAX_INT = 2147483647
    MIN_INT = -2147483647

    def reverse(self, x: int) -> int:
        abs_x = abs(x)

        reversed_x = 0
        while abs_x != 0:
            head = abs_x % 10
            abs_x //= 10
            reversed_x = reversed_x * 10 + head

            if reversed_x < self.MIN_INT or reversed_x > self.MAX_INT:
                return 0

        if x > 0:
            return reversed_x

        return -reversed_x
