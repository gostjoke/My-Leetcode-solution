# 20250627
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root)->list:
            if root:
                dfs(root.left)
                dfs(root.right)
                ans.append(root.val)

        dfs(root)
        return ans
