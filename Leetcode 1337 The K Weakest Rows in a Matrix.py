# 05/17/2024
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        g = [(sum(i),ind) for ind, i in enumerate(mat)]
        g.sort(key =lambda x:(x[0],x[1]))
        return [row[1] for row in g][:k]
