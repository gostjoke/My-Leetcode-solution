# 06/12/2024

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(i) for i in nums]
        score = 0
        for i in zip(*nums):
            score = score + max(i)
        return score
