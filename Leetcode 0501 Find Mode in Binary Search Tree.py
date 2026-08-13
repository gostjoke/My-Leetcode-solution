# 2026/08/12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]

        self.prev = None
        self.count = 0 
        self.max_count = 0
        self.modes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            if self.prev is not None and node.val == self.prev:
                self.count += 1
            else:
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)
            
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.modes
