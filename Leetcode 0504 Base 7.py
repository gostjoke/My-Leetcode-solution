# 08/08/2024
class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        ans = ""
        while n:
            n, remain = divmod(n, 7)
            ans = str(remain) + ans
        return "-" * (num < 0) + ans or "0"
