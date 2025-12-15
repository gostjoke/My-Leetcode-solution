# 2025/12/15
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low % 2 == 1:
            ans+=1
            low = low+1
        if high % 2 == 1:
            ans+=1
            high = high-1

        ans += (high - low) / 2
        return int(ans)
