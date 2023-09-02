from typing import List


class Solution:
    def isCommonPrefix(self, prefix: str, strs: List[str]):
        for s in strs:
            if not s.startswith(str(prefix)):
                return False

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        for char in strs[0]:
            if self.isCommonPrefix(common_prefix + char, strs):
                common_prefix += char
            else:
                return common_prefix

        return common_prefix
