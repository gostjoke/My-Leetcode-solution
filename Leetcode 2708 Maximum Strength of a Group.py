# 20250805
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        postive = []
        negative = []

        for i in nums:
            if i > 0:
                postive.append(i)
            if i < 0:
                negative.append(i)

        negative.sort()

        if len(negative) % 2 ==1:
            negative.pop()

        if not negative and not postive:
            return 0

        ans = 1
        for i in (postive + negative):
            ans *= i
        
        return ans
