# 2025/01/14

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        ans = [float('inf'), float('inf')]
        for i in range(0, len(nums)):
            if ans[0] >= nums[i]:
                ans[0] = nums[i]
            elif ans[1] >= nums[i]:
                ans[1] = nums[i]
            else:
                return True
        return False
    
