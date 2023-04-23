#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :35.8%%, Memory 13.8 Beats 96.84%
@date         :2023/04/22 22:01:20

'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        #### first solution
        # a = [] # for a
        # b = [] # 
        # for i in nums:
        #     if str(i) not in a:
        #         a.append(str(i))
        #     else:
        #         b.append(str(i))
        
        # for i in nums:
        #     if str(i) not in b:
        #         return int(i)
        
        #### second solution 
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key, value in dic.items():
            if value == 1:
                return key

print(Solution().singleNumber(nums = [2,2,1]))
