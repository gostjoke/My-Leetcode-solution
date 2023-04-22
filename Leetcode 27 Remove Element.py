#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :7.45%, Memory14.9 Beats 7%
@date         :2022/10/23 11:31:20

'''
# It is easy but very slow, maybe need to use 2 pointer
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)