# 2025/01/15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # 遞迴計算左右子樹深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 更新最大直徑
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            # 返回節點的深度
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.max_diameter
