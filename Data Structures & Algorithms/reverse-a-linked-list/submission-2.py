# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        original_vals = []
        while current:
            original_vals.append(current.val)
            current = current.next

        new_head = ListNode(val=original_vals[-1])
        current_node = new_head
        for i in range(len(original_vals)-2, -1, -1):
            new_node = ListNode(val=original_vals[i])
            # if new_head == new_node:
            #     new_head = new_node
            # next_node = ListNode(val=original_vals[i-1])
            # if not next_node:
            #     new_node.next = next_node
            current_node.next = new_node
            current_node = new_node

        return new_head
