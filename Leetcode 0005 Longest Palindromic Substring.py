# 06/03/2024  
# thanks to https://www.youtube.com/watch?v=vjzVfmWjJg8
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(l, r):
            nonlocal max_l, max_r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l +1 > max_r - max_l + 1:
                    max_l, max_r = l, r
                l, r = l - 1, r + 1

        max_l = max_r = 0
        for i in range(len(s)):
            is_palindrome(i, i)
            is_palindrome(i, i+1)
        return s[max_l:max_r + 1]
