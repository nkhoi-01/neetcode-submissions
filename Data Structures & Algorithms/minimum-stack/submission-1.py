class MinStack:

    def __init__(self):
        self.main = []
        self.min = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.min:
            self.min.append(val)
            return
        if val <= self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.main.pop()
        self.min.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.min[-1]
