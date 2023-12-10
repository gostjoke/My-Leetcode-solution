"""
12/09/2023
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n

        # right side
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1

        # left side
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i + 1] + 1)

        return sum(result)
