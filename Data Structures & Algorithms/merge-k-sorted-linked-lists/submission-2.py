# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ///
        # **Brute force approach**
        # ///
        nodes = []
        for list_nodes in lists:
            cur = list_nodes
            while cur:
                nodes.append(cur.val)
                cur = cur.next
        
        if not nodes:
            return None

        nodes_sorted = sorted(nodes)
        dummy_head = ListNode()
        cur_node = dummy_head
        for node_value in nodes_sorted:
            new_node = ListNode(val=node_value)
            cur_node.next = new_node
            cur_node = cur_node.next
        
        return dummy_head.next
        
        # ///
        # **Iteration approach**
        # ///
        # dummy = ListNode()
        # cur = dummy

        # while True:
        #     min_list = -1

        #     for i in range(len(lists)):

        #         if not lists[i]:
        #             continue

        #         if min_list == -1 or lists[min_list].val > lists[i].val:
        #             min_list = i

        #     if min_list == -1:
        #         break

        #     cur.next = lists[min_list]
        #     lists[min_list] = lists[min_list].next
        #     cur = cur.next

        # return dummy.next