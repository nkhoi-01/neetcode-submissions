class Node:
    def __init__(self, value=-1):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new_node = Node(value=value)

        # In case where the Deque is empty, 'tail' would be the 'head'
        tail = self.right.prev
        tail.next = new_node
        new_node.prev = tail
        
        # Implicitly update the new tail
        new_node.next = self.right
        self.right.prev = new_node

        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value=value)

        head = self.left.next
        self.left.next = new_node
        new_node.prev = self.left
        new_node.next = head
        head.prev = new_node

        self.size += 1


    def pop(self) -> int:
        target = self.right.prev

        new_tail = self.right.prev.prev
        # if the Deque is empty
        if not new_tail:
            return -1

        new_tail.next = self.right
        self.right.prev = new_tail

        self.size -= 1
        
        return target.value

    def popleft(self) -> int:
        target = self.left.next

        new_head = self.left.next.next
        # if the Deque is empty
        if not new_head:
            return -1

        self.left.next = new_head
        new_head.prev = self.left

        self.size -= 1

        return target.value
