# 2025/06/12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        self.ans = True
        def dfs(root):
            l, r = 0, 0
            if root.left: # check left node
                l += dfs(root.left)
            if root.right: # check right node
                r += dfs(root.right)
            if abs(r-l) > 1:
                self.ans=False

            return max(r, l) + 1
        dfs(root)
        return self.ans
        
