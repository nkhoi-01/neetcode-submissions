class Solution:
    def isValid(self, s: str) -> bool:
        dict_s = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        closing = dict_s.keys()
        opening = dict_s.values()
        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack) != 0 and stack[-1] == dict_s[s[i]]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False

        return True