# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node:
                return 0
            cur = cur * 10 + node.val
            if not node.right and not node.left:
                return cur
            return dfs(node.right, cur) + dfs(node.left, cur)
        return dfs(root, 0)

