'''
07/18/2023
'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        
        
        for i in range(n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-(j**2)]+1)
                j += 1

        return dp[-1] 
