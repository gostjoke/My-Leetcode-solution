# 20250828

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: 找下降點
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # Step 2: 找到比 nums[i] 大的最小數
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3 swap
            nums[i], nums[j] = nums[j], nums[i]
        # reverse i+1
        nums[i+1:] = reversed(nums[i+1:])



