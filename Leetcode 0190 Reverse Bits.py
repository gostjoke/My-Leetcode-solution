"""
06/05/2023
explain@: it is my best understanding

Time complexity:
O(1)

Space complexity:
O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n).replace("0b", "").zfill(32)[::-1],2)