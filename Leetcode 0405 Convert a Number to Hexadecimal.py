"""
12/10/2023
"""

class Solution:
    def toHex(self, num: int) -> str:
        hex ="0123456789abcdef"
        ans=""
        if num == 0: return "0"
        elif num < 0:
            num += 2**32
        while num:
            ans += hex[num%16]
            num//=16
        return ans[::-1]
