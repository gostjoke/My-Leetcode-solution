'''
06/21
use binary search to do it
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ## binary
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right+left) // 2 
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left

# my first solution passed but not good, use extra space

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = (-2)**31
        index = 0
        for ind, i in enumerate(nums):
            if i > peak:
                peak =i
                index = ind
        return index
