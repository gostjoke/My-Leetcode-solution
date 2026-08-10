# 2026/08/10
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
