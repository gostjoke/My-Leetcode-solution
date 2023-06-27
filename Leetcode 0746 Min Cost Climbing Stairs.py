"""
06/27/2023
it is very similar to left down minium matrix
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dp =[0] * len(cost)
        
        dp[0] = cost[0]

        if len(cost) >= 2:
            dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        print(dp)
        return min(dp[-1], dp[-2])
