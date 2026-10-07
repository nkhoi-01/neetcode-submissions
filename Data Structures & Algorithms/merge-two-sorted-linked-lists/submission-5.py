# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        # Decide which list nosde has the final head (smallest val)
        if list1.val <= list2.val:
            head = list1
            current_node = list1
            other_node = list2
        else:
            head = list2
            current_node = list2
            other_node = list1

        # Require current_node.next to not falsy so current_node.next.val
        #  won't evaluate to None.val and subsequently returned Error
        while current_node.next and other_node:
            # The first node of current_node is already correctly positioned
            #  need to decide the other node comes before or after the
            #  next value of current_node
            if current_node.next.val <= other_node.val:
                current_node = current_node.next
            else:
                # Store the reference to the remainder of the other list
                next_other_node = other_node.next

                other_node.next = current_node.next
                current_node.next = other_node
                current_node = other_node

                other_node = next_other_node

        # Guard where current list contains only 1 node so current.next
        #  is falsy so the while loop is not run
        # Current list always contains the final head with the smallest 
        #  initial val
        if other_node:
            current_node.next = other_node

        return head