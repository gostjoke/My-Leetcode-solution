# 2026/01/22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, nums):
            print(nums)
            if not root:
                return []
            localnums = nums + [str(root.val)]
            if not root.right and not root.left:
                return ["->".join(localnums)]
            return dfs(root.left, localnums) + dfs(root.right, localnums)
        return dfs(root, [])
