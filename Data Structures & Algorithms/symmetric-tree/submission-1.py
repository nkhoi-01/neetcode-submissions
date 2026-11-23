from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # ///
        # **Iterative approach**
        # ///
        # q = deque([root, root])

        # while q:
        #     tree_left = q.popleft()
        #     tree_right = q.popleft()

        #     if tree_left is None and tree_right is None:
        #         continue
        #     if tree_left is None or tree_right is None:
        #         return False
        #     if tree_left.val != tree_right.val:
        #         return False
            
        #     q.append(tree_left.left)
        #     q.append(tree_right.right)
        #     q.append(tree_left.right)
        #     q.append(tree_right.left)

        # return True

        # ///
        # **Recursion approach**
        # ///
        def is_mirror(tree_left, tree_right):
            if tree_left is None and tree_right is None:
                return True
            if tree_left is None or tree_right is None:
                return False
            
            return (
                (tree_left.val == tree_right.val)
                and is_mirror(tree_left.left, tree_right.right)
                and is_mirror(tree_left.right, tree_right.left)
            )

        return is_mirror(root, root)

