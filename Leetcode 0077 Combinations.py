"""
06/04/2023
explain: use backtrack to see
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []
        self.backtrack(1, [], n, k, results)
        return results
    def backtrack(self, start, comb, n, k, results):
        if len(comb) == k:
            results.append(comb[:])  # [:] copy will not be influence
            return
        for i in range(start, n+1):
            
            comb.append(i)
            print(comb)
            self.backtrack(i+1, comb, n, k, results)
            comb.pop() # take out last one

n = 6
k = 4
print(Solution().combine(n, k))