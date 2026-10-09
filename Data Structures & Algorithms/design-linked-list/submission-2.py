class ListNode:
    def __init__(self, val=-1, next=None, prev=None):
        self.value = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if self.length == 0:
            return -1

        if index < 0 or index >= self.length:
            return -1

        current = self.head
        for i in range(index + 1):
            current = current.next
            if not current:
                return -1
            
        return current.value

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val=val)
        current_head = self.head.next
        self.head.next = new_head
        new_head.prev = self.head
        new_head.next = current_head

        if current_head:
            current_head.prev = new_head
        else:
            self.tail = new_head
        
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val=val)
        current_tail = self.tail
        self.tail.next = new_tail
        new_tail.prev = current_tail
        self.tail = new_tail
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val=val)
            return

        if self.length == index:
            self.addAtTail(val=val)
            return

        if index + 1 > self.length:
            return
        
        new_node = ListNode(val=val)
        current_node = self.head
        for i in range(index + 1):
            current_node = current_node.next
        prev_node = current_node.prev

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current_node
        current_node.prev = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.length == 0:
            return

        if index + 1 > self.length:
            return

        prev_node = None
        to_delete = self.head
        for i in range(index + 1):
            prev_node = to_delete
            to_delete = to_delete.next
        
        next_node = to_delete.next
        prev_node.next = next_node
        if not next_node:
            self.tail = prev_node
        else:
            next_node.prev = prev_node
        
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)