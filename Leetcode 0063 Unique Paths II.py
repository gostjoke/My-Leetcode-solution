"""
06/29/2023
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1 or obstacleGrid[0][0] == -1:
            return 0
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1

        for r in range(n):
            for k in range(m):
                if obstacleGrid[r][k] == 0: # if not obstacleGrid
                    if r - 1 >= 0:
                        dp[r][k] += dp[r-1][k]
                    else: 0
                    if k - 1 >= 0:
                        dp[r][k] += dp[r][k-1]
                    else: 0
        return dp[-1][-1]
