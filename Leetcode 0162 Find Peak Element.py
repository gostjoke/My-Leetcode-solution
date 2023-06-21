'''
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ## binary
        left = 0
        right = len(nums)-1
        while left < right:
            mid = ((right+left) // 2 )
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left
