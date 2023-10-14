"""
10/14/2023

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_result = nums[0]
        for i in range(1, len(nums)):
            # if current < max then we reset the start
            max_current = max(nums[i], nums[i]+max_current)
        
            if max_current > max_result:
                max_result = max_current
        return max_result
