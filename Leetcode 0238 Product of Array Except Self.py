'''
07/06/2023
'''

### my original code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        zero = 0
        for i in nums:
            if i != 0:
                n *= i
            if i == 0:
                zero += 1
            if zero == 2: ### if we have 2 0 it must be all zerop
                return [0]*len(nums)

        if zero == 1: # if we have one 0 it must be only that 0 num is not zero
            for ind, j in enumerate(nums):
                if j != 0:
                    nums[ind] = 0
                else:
                    nums[ind] = n
            return nums
        else: # if we have no 0 just divide its original number.
            count = 0
            ans = [n] * len(nums)
            for x, y in zip(nums, ans):
                ans[count] = int(y/x)
                count += 1

            return ans


### ChatGPT improve my code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
    
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result
