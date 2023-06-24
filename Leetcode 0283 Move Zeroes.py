"""
06/24/2023
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[a] = nums[a], nums[i]
                a+=1
