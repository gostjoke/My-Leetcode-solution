### 2026/07/20

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tmp_grid=[]
        for i in range(m):
            for j in range(n):
                tmp_grid.append(grid[i][j])
        for a in range(k):
            b = tmp_grid.pop()
            tmp_grid.insert(0, b)
        result = []
        tmp = []
        for index, i in enumerate(tmp_grid):
            tmp.append(i)
            if index % n == n-1:
                result.append(tmp)
                tmp = []
        return result
