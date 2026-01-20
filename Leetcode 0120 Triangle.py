# 2026/01/19
class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        # from 2nd bottom  to top
        for i in range(len(tri)-2, -1, -1):
            for j in range(len(tri[i])):
                tri[i][j] += min(tri[i+1][j], tri[i+1][j+1])
        return tri[0][0]
