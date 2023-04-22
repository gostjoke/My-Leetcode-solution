#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :62.65%, Memory14.9 Beats 27%
@date         :2023/04/22 11:31:20

'''
#i know it is good with binary search, try later
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for ind, i in enumerate(nums):
            if i >= target:
                return ind
        else:
            return len(nums)