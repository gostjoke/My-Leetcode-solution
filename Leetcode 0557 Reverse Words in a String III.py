"""
08/15/2023
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split(" ")
        for index, i in enumerate(ans):
            ans[index] = i[::-1]

        return " ".join(ans)
