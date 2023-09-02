class Solution:
    """
    Complexity Analysis
    -------------------
    Time complexity O(n)
    Space complexity O(1)
    """

    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, roman_number: str) -> int:
        result = 0
        idx = 0
        last_idx = len(roman_number) - 1

        while idx <= last_idx:
            one_digit = roman_number[idx]
            if idx == last_idx or last_idx == 0:
                result += self.dictionary[one_digit]
                break

            two_digits = one_digit + roman_number[idx + 1]
            if two_digits in self.dictionary:
                result += self.dictionary[two_digits]
                idx += 2
            else:
                result += self.dictionary[one_digit]
                idx += 1

        return result
