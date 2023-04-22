#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :42.6%, Memory14.9 Beats 89.67%
@date         :2023/04/20 11:31:20
@author       : 
@version      :1.0
'''



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        counter = 0
        for i in range(len(nums)): # only check the list first one if it does not match then pop it
            tmp = nums[0]
            nums.pop(0)
            counter += 1 # need to check how many eles got kick out
            if (target -tmp) in nums: 
                ans2 = nums.index(target -tmp) + counter
                return [i,ans2]
