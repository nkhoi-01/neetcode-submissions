class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        len_needle = len(needle)
        for i in range(len(haystack) - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
            else:
                continue
                
        return -1