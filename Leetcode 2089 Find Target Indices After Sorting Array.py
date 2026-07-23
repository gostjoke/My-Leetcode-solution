# 2026/07/23

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        ans = []
        for index, n in enumerate(nums):
            if n == target:
                ans.append(index)
        return ans
