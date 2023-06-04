"""
06/04/2023
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False

        return s in (s+s)[1:-1]