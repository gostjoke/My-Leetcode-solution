# still a little confused
# 2026/01/18
class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = []
        for i in range(1 << n):  # 1 << n 就是 2 的 n 次方
            result.append(i ^ (i >> 1))
        return result
