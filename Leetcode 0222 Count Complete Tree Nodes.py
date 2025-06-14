# 20250613 
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def GetHeight(node):
            h = 0
            while node:
                node = node.left
                h+=1
            return h
        
        if not root:
            return 0
        
        left_height = GetHeight(root.left)
        right_height = GetHeight(root.right)
        if left_height == right_height:
            return 2**left_height + self.countNodes(root.right)
        else:
            return 2**right_height + self.countNodes(root.left)
