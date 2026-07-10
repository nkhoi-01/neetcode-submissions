class PageNode:
    def __init__(self, value='', back=None, forward=None):
        self.url = value
        self.back = back
        self.forward = forward

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = PageNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node = PageNode(url)

        curr = self.current
        curr.forward = new_node
        new_node.back = curr
        self.current = new_node

    def back(self, steps: int) -> str:
        if steps <= 0:
            return self.current.url

        curr = self.current
        while steps > 0:
            if not curr.back:
                break
            curr = curr.back
            steps -= 1
        self.current = curr

        return curr.url

    def forward(self, steps: int) -> str:
        if steps <= 0:
            return self.current.url

        curr = self.current
        while steps > 0:
            if not curr.forward:
                break
            curr = curr.forward
            steps -= 1
        self.current = curr

        return curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)