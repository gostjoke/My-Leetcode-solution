'''
07/06/2023
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        zero = 0
        for i in nums:
            if i != 0:
                n *= i
            if i == 0:
                zero += 1
            if zero == 2:
                return [0]*len(nums)
        if zero == 1:
            for ind, j in enumerate(nums):
                if j != 0:
                    nums[ind] = 0
                else:
                    nums[ind] = n
            return nums
        else:
            count = 0
            ans = [n] * len(nums)
            for x, y in zip(nums, ans):
                ans[count] = int(y/x)
                count += 1

            return ans
