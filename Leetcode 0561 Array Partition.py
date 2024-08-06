# 08/06/2024
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(int(len(nums)/2)):
            count += nums[i*2]
        return count
         
