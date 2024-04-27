## 04/27/2024

class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        memo={}
        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left,right)]
            if left == right:
                return p[left]
            score_left = p[left] - dfs(left+1, right)
            score_right = p[right] - dfs(left, right-1)
            memo[(left,right)] = max(score_left, score_right)
            return memo[(left,right)]
        return dfs(0, len(p)-1)>0
      
## bez Alice always win, first chose always win
class Solution:
    def stoneGame(self, p: List[int]) -> bool:
      return True
