#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :use 2 pointer to resolve
@date         :2023/05/31 13:38:23
@version      :1.0
'''

# Definition for singly-linked list.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        pointer = 0
        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1
