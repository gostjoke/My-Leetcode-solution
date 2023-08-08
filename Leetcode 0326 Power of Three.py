"""
08/08/2023
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        while n > 0:
            n /= 3
            if int(n) != n:
                return False
            elif n == 1:
                return True
