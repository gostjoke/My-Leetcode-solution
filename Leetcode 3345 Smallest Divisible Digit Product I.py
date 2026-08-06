# 2026/08/06

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            tp = 1
            for num in str(i):
                tp *= int(num)
            if tp % t == 0:
                return i
