"""
09/17/2023

"""

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        first, last = 1, n
        while first <= last:
            mid = first + (last - first)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                last = mid - 1
            else:
                first = mid + 1
        return -1
