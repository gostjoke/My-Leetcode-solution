## 20250623

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_diff = -1
        for i in range(len(nums)):
            if nums[i] > min_num:
                max_diff = max((nums[i]-min_num), max_diff)
            else:
                min_num = nums[i]
        return max_diff
                
