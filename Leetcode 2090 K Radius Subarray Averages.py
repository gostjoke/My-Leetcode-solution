"""
6/20/2023 1:31AM
thanks to Rosa's solution
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 2 pointer slide window
        if k == 0 :
            return nums
        elif len(nums) < k*2+1:
            return [-1]*len(nums) 

        res = [-1]*len(nums)
        left, curwindowsum, diameter = 0, 0, k*2+1
        for right in range(len(nums)):
            curwindowsum += nums[right]
            if (right-left)+1 >= diameter:
                res[left+k] = curwindowsum//diameter
                curwindowsum -= nums[left]
                left += 1
        return res
