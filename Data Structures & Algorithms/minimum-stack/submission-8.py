class MinStack:

    def __init__(self):
        self.diff_stack = []
        self.cur_min = False

    def push(self, val: int) -> None:
        if not self.diff_stack:
            self.diff_stack.append(0)
            self.cur_min = val
        else:
            diff = val - self.cur_min
            self.diff_stack.append(diff)
            
            if val < self.cur_min:
                self.cur_min = val

    def pop(self) -> None:
        if not self.diff_stack:
            return
        
        popped = self.diff_stack.pop()
        if popped < 0:
            # diff = val - min. If we pop a negative value, it means
            #  the popped value is for the current min 'self.cur_min'. To
            #  restore the previous min, look at the provided equation 
            #  above `diff = val - min`, it is equivalent to 
            #  `min = val - diff`, or `prev_min = self.cur_min - popped`
            self.cur_min = self.cur_min - popped

    def top(self) -> int:
        if not self.diff_stack:
            return

        res = False
        if self.diff_stack[-1] >= 0:
            res = self.diff_stack[-1] + self.cur_min
        else:
            res = self.cur_min

        return res

    def getMin(self) -> int:
        return self.cur_min
