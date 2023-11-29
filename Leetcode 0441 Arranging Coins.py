"""
11/29/2023
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        result = 0
        counter = 1
        while n > 0:
            n -= counter
            counter += 1
            if n >= 0:
                result += 1
        return result
