# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ///
        # **Iteration approach**
        # ///
        # travel to the leftmost tree node
        # current = root
        # stack = []
        # result = []
        # while current:
        #     stack.append(current)
        #     current = current.left
        #     if not current:
        #         popped = stack.pop()
        #         result.append(popped.val)
        #         while not popped.right and stack:
        #             popped = stack.pop()
        #             result.append(popped.val)
        #         current = popped.right
        
        # return result

        # ///
        # **Recursion approach**
        # ///
        if not root:
            return []
        res = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
