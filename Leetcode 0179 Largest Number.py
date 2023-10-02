"""
10/01/2023
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(n1, n2):
            if int(n1+n2) > int(n2+n1):
                return -1
            if int(n2+n1) > int(n1+n2):
                return 1
            return 0

        nums = [str(i) for i in nums]

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)      
        
