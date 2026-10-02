class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        for left in range(len(haystack) - size + 1):
            if needle == haystack[left:left+size]:
                return left
        return -1