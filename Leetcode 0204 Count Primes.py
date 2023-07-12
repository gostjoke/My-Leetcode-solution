'''
07/12/2023
'''

"""
n = 10
dp[2]
[False, False, True, True, False, True, False, True, False, True]
dp[3]
[False, False, True, True, False, True, False, True, False, False]
"""


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        
        for i in range(2, int(n**0.5) +1):
            if dp[i]:
                dp[i*i:n:i] = [False] * len(dp[i*i:n:i])
            print(dp)

        return dp.count(True)    
