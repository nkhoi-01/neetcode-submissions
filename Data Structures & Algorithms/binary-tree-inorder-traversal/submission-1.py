# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # travel to the leftmost tree node
        current = root
        stack = []
        result = []
        while current:
            stack.append(current)
            current = current.left
            if not current:
                popped = stack.pop()
                result.append(popped.val)
                while not popped.right and stack:
                    popped = stack.pop()
                    result.append(popped.val)
                current = popped.right
        
        return result