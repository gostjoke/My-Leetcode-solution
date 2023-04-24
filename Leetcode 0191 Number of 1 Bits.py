#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :Runtime 27 ms Beats 92.82%, Memory 13.7 Beats 89.9%
@date         :2023/04/23 17:25:20
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    
# not really hard but binary input is not any type XD so I am a little confused until see others answer.