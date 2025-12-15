# 2025/12/15
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # slide window
        n = len(prices)
        if n < 2:
            return 1
        ans = 1
        curr = 1
        for i in range(1, n):
            if prices[i-1] - prices[i]==1:
                curr+=1
            else:
                curr=1
            ans+=curr
        return ans
