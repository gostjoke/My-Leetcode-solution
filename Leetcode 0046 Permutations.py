#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/24 17:06:28

it is obviously Combinatorics problems, so nums = ["A","B","C"]
the first position of list 

nums[0] has 3 choose
nums[1] has 2 choose
nums[2] has 1 choose
'''


from itertools import permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums,len(nums)))

a = Solution().permute(nums=[1,2,3])
print(a)