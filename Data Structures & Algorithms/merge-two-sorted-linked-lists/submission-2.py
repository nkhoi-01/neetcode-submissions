# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Standard Approach
        # dummy = ListNode(-1)
        # curr = dummy
        # curr1 = list1
        # curr2 = list2
        # while curr1 or curr2:
        #     if not curr1:
        #         curr.next = curr2
        #         break
        #     if not curr2:
        #         curr.next = curr1
        #         break
        #     if curr1.val < curr2.val:
        #         curr.next = curr1
        #         curr = curr.next
        #         curr1 = curr1.next
        #     elif curr1.val > curr2.val:
        #         curr.next = curr2
        #         curr = curr.next
        #         curr2 = curr2.next
        #     else:
        #         curr.next = curr1
        #         curr = curr.next
        #         curr1 = curr1.next
        #         curr.next = curr2
        #         curr = curr.next
        #         curr2 = curr2.next
        # return dummy.next

        # Recursion Approach
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        elif list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2