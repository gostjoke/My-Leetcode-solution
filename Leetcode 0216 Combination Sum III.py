# 08072024 
# not totally understand ...
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(cur, n, i):
            if k == len(cur):
                if n == 0:
                    ans.append(cur.copy())
                return
            for num in range(i, 10):
                cur.append(num)
                dfs(cur, n-num, num+1)
                cur.pop()
            
        dfs([], n, 1)
        return ans
