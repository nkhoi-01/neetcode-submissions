def is_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if is_integer(ops):
                stack.append(int(ops))
            if ops == '+':
                stack.append(stack[-1] + stack[-2])
            if ops == 'D':
                stack.append(stack[-1] * 2)
            if ops == 'C':
                stack.pop()

        return sum(stack)