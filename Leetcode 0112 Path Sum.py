'''
2023/06/21
do not really understand need more practice
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # edge case
            return False

        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()

            if not node.left and not node.right and val == targetSum:
                return True

            if node.left:
                stack.append((node.left, val + node.left.val))
            
            if node.right:
                stack.append((node.right, val + node.right.val))
        
        return False
