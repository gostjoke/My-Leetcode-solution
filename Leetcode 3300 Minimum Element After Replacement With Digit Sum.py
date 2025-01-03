# 2025/01/03
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10000
        for n in nums:
            tmp = 0
            for i in str(n):
                tmp += int(i)
            if tmp < ans:
                ans = tmp
        return ans
