"""
08/13/2023
it is Base-26

"BAC" means ("B" * 26^2) + ("A" * 26^1) + ("C"*26^0)
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ind, i in enumerate(columnTitle[::-1]):
            ans += (ord(i) - 64)*(26**ind)
        return ans
