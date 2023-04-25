#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
17. Letter Combinations of a Phone Number
Beats
99.91%
Memory
13.8 MB
Beats
63.96%
@date         :2023/04/24 11:47:20
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        zero_check = 0
        no_start = 0
        ans = ""
        for i in s:
            if i == "0":
                zero_check =1
            elif i != "0" and i.isnumeric():
                no_start = 1
            elif zero_check == 1 and i.isnumeric() is False and no_start != 1:
                return 0
        
        ##### "    -88827   5655  U"
        space_check = 0
        no_start = 0
        ans = ""
        check = 0
        no_num = 0
        
        for i in s: 
            
            if space_check == 0 and i == " ":
                space_check = 1
            if i == " " and no_start != 0 and i != "+" and i != "-":
                break
            elif no_num == 2:
                break
            elif no_num == 1 and i.isnumeric() is False:
                break
            elif i == "+":
                no_num += 1
            elif i == "-" and no_start ==0:
                no_num += 1
                check = 1
            elif i.isnumeric() is False and i !=" ":
                break
            elif i != " ":
                ans += i
                no_start = 1      
        
        try:
            b = int(ans)
        except:
            return 0
        if check == 1:
            b *= (-1)

        if b < (-2)**31:
            return (-2)**31
        elif b > (2**31) - 1:
            return (2**31) - 1
        else:
                return b