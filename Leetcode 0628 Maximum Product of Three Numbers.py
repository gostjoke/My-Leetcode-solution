# 2026/08/10
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # 3 positive max, or  2 min + 1 max
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
