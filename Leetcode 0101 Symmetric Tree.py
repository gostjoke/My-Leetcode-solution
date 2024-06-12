# 06/12/2024

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_mirror(r1, r2):
            if r1 == None and r2 == None:
                return True
            if r1 != None and r2 == None or r1 == None and r2 != None:
                return False
            if r1.val == r2.val:
                return check_mirror(r1.left, r2.right) and check_mirror(r1.right, r2.left)
        
        return check_mirror(root, root)
