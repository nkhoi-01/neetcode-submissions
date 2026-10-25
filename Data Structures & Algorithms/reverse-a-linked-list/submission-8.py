# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ///
        # ** Brute-force approach **
        # ///
        if not head:
            return
        if not head.next:
            return head

        list_vals = []
        current_org = head
        while current_org:
            list_vals.append(current_org.val)
            current_org = current_org.next

        rev_list = list_vals[::-1]
        new_head = ListNode(val=rev_list[0])
        current = new_head
        for value in rev_list[1:]:
            new_node = ListNode(val=value)
            current.next = new_node
            current = current.next

        return new_head


        # ///
        # ** Recursion approach **
        # ///
        #TODO