# 0809/2024

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        m = len(self.grid)
        n = len(self.grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == value:  
                    if i > 0:
                        res += self.grid[i-1][j]  
                    if i < m-1:
                        res += self.grid[i+1][j]  
                    if j > 0:
                        res += self.grid[i][j-1]  
                    if j < n-1:
                        res += self.grid[i][j+1]  
        return res

    def diagonalSum(self, value: int) -> int:
        m = len(self.grid)
        n = len(self.grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == value:  
                    if i > 0 and j > 0:
                        res += self.grid[i-1][j-1] 
                    if i < m-1 and j < n-1:
                        res += self.grid[i+1][j+1]  
                    if i < m-1 and j > 0:
                        res += self.grid[i+1][j-1]  
                    if i > 0 and j < n-1:
                        res += self.grid[i-1][j+1] 
        return res


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
