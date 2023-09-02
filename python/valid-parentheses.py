MAPPING = {
    "}": "{",
    ")": "(",
    "]": "["
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        for idx in range(1, len(s)):
            char = s[idx]
            if char in MAPPING and stack:
                stack_top_char = stack.pop()

                # Should be closing parenthesis here. If is not no reason to iterate further.
                if MAPPING[char] != stack_top_char:
                    return False

            else:
                stack.append(char)

        if stack:
            return False

        return True
