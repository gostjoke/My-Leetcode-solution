"""
# 2026/01/13
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root)
        return root
    def dfs(self, root):
        # 完全二滿足樹 確保左邊在即可
        # 初始下next皆為空
        if not root or not root.left:
            return 
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left

        # 先left 後right
        self.dfs(root.left)
        self.dfs(root.right)
