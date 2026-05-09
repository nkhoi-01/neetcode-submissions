# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        reversed_values = []
        while head:
            values.append(head.val)
            head = head.next
        if not values:
            return None
        for i in range(len(values)-1, -1, -1):
            reversed_values.append(values[i])
        new_head = ListNode(reversed_values[0])
        current_head = new_head
        for val in reversed_values[1:]:
            current_head.next = ListNode(val)
            current_head = current_head.next
        return new_head
            