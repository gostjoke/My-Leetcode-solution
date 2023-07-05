'''
07/05/2023
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        ans = []
        for i in range(n):
            for j in range(n):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]


#####
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for r in matrix:
            res += r
        return sorted(res)[k-1]
