class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in matrix:
            if min(i) == max([j[i.index(min(i))] for j in matrix]):
                return [min(i)]
