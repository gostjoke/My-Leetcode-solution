# 05/18/2024
# dp solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]
        for c in coins:
            for small_amount in range(c, amount+1):
                dp[small_amount] += dp[small_amount -c]
        return dp[-1]

