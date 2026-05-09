class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        brac_dict = {
                     '(': ')', 
                     '[': ']',
                     '{': '}',
                     }
        opening = [key for key, value in brac_dict.items()]
        closing = [value for key, value in brac_dict.items()]
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
                continue
            elif c in closing:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if brac_dict[top] != c:
                    return False
        return len(stack) == 0