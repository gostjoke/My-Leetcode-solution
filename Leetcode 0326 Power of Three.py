"""
08/08/2023
this can use in any powerofnumber
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

Leetcode power of four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        while n > 0:
            n /= 4
            if int(n) != n:
                return False
            elif n == 1:
                return True
