# 2025/06/11
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0 or s[0]=="0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 # empty s
        dp[1] = 1 # only 1 solution
        for i in range(2, n+1):
            one_dig = int(s[i-1])
            two_dig = int(s[i-2:i])
            
            if one_dig != 0:
                dp[i] += dp[i - 1]
            
            if 10 <= two_dig <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

