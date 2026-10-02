class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
            if not current:
                return -1
            
        return current.value

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
            return

        new_head = ListNode(val)
        old_head = self.head
        new_head.next = old_head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
            return

        new_tail = ListNode(val)
        old_tail = self.tail
        old_tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        remove = self.head
        for i in range(index):
            prev = remove
            remove = remove.next
            if not remove:
                return False

        if index == 0:
            self.head = remove.next
            return True
            
        prev.next = remove.next
        if remove == self.tail:
            self.tail = remove.next
            if prev == self.head:
                self.tail = self.head

        return True

    def getValues(self) -> List[int]:
        if not self.head:
            return []

        current = self.head
        res = []
        while current:
            res.append(current.value)
            current = current.next
        
        return res
        
