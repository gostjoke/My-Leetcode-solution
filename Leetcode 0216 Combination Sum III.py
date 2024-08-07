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

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if len(path) == k and target == 0:
                res.append(path)
                return
            if len(path) > k or target < 0:
                return
            
            for i in range(start, 10):
                backtrack(i + 1, path + [i], target - i)
        
        res = []
        backtrack(1, [], n)
        return res
