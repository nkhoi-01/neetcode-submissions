class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode(val=homepage)
        self.current = self.left

    def visit(self, url: str) -> None:
        current = self.current
        current_next = current.next
        page = ListNode(val=url)
        current.next = page
        page.prev = current
        self.current = page

        cleared_forward = 0
        while current_next:
            cleared_forward += 1
            current_next = current_next.next

    def back(self, steps: int) -> str:
        current = self.current
        while steps > 0 and current:
            if not current.prev:
                break
            current = current.prev
            steps -= 1
        self.current = current
        
        return current.value

    def forward(self, steps: int) -> str:
        current = self.current
        
        while steps > 0 and current:
            if not current.next:
                break
            current = current.next
            steps -= 1
        self.current = current

        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)