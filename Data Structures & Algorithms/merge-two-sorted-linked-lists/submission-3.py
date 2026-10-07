# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        node_l1 = list1
        node_l2 = list2

        current = dummy
        # TODO
        while node_l1 and node_l2:
            if node_l1.val <= node_l2.val:
                current.next = node_l1
                node_l1 = node_l1.next
            else:
                current.next = node_l2
                node_l2 = node_l2.next

            current = current.next

        if node_l1:
            current.next = node_l1
        if node_l2:
            current.next = node_l2

        return dummy.next
        