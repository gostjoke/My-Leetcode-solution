# 2026/03/12
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      : Beat 59%
@date         :2023/04/25 
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False


## I alway use set() to remove duplicates, so I immediately think this
