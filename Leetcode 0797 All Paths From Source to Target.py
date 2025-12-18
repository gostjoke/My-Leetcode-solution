# 2025/12/18
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0] # walked
        n = len(graph)-1 # 4
        def dfs(node):
            if node == n:
                res.append(path.copy())
                return
            for nxt in graph[node]:
                path.append(nxt) # move 1
                dfs(nxt) # move to next
                path.pop() # move back
        dfs(0)
        return res
