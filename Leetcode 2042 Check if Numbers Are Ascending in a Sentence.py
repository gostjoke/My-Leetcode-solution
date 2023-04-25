#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/24 11:31:20
'''

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        li = s.split(" ")
        curr = 0
        for i in li:
            if i.isnumeric():
                if int(i) > curr:
                    curr = int(i)
                else:
                    return False
        return True