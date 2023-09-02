class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word1_last_idx = len(word1) - 1
        word2_last_idx = len(word2) - 1

        result = []

        while i <= word1_last_idx and i <= word2_last_idx:
            result.append(word1[i])
            result.append(word2[i])
            i += 1

        if i <= word1_last_idx:
            for x in range(i, word1_last_idx + 1):
                result.append(word1[x])
        elif i <= word2_last_idx:
            for x in range(i, word2_last_idx + 1):
                result.append(word2[x])

        return "".join(result)
