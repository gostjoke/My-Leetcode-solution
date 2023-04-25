"""
04/24/2023
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1 

        for i, a in dic.items():
            if a*2 > len(nums):
                return i
