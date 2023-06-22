'''
06/22/2023
n = 5
dp = [1, 1, 0, 0, 0, 0]

dp[2]：
dp = [1, 1, 2, 0, 0, 0]

dp[3]：
dp = [1, 1, 2, 3, 0, 0]

dp[4]：
dp = [1, 1, 2, 3, 5, 0]

dp[5]：
dp = [1, 1, 2, 3, 5, 8]
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1 , 1
        if len(dp) <= 2:
            return 1
        counter = 2
        for i in dp[2:]:
            dp[counter] = dp[counter-1] + dp[counter-2]
            counter += 1 
        return dp[-1]

### better solution
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        
        for i in range(n-1):
            print(one, two)
            one, two = two, one + two
        return two
