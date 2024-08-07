# 08/07/2024

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        lastPos, lastNeg = 0, 0 # the index
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if diff < 0:
                dp[i] = 1 + dp[lastPos]
                lastNeg = i
            if diff > 0:
                dp[i] = 1 + dp[lastNeg]
                lastPos = i
        return max(dp)

            
