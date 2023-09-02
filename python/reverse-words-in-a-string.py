class Solution:
    def reverseWords(self, s: str) -> str:
        """
        "the sky is blue"
        """

        last_idx = len(s) - 1
        i = 0
        j = last_idx

        # Trim left whitespaces
        while s[i] == " ":
            i += 1

        # Trim right whitespaces
        while s[j] == " ":
            j -= 1

        sentence = []
        word = []

        while i <= j:
            if s[j] == " " and word == []:
                j -= 1
                continue
            elif s[j] == " ":
                sentence.append("".join(word))
                word = []
            else:
                word = [s[j]] + word

            j -= 1

        sentence.append("".join(word))

        return " ".join(sentence)
