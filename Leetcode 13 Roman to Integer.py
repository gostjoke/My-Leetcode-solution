#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file         :Leetcode 13 Roman to Integer.py
@explain      :
@date         :2023/04/21 11:31:20
@author       :
@version      :1.0
'''

"""
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dic={"I":1,
            "V":5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            "T":90,
            "G":900,
            "B":9,
            "Y":400,
            "U":40}

        s = s.replace("IV","IIII")
        s = s.replace("XC","T")
        s = s.replace("CM","G")
        s = s.replace("IX","B")
        s = s.replace("CD","Y")
        s = s.replace("XL","U")
        ans = 0
        for i in s:
            ans += dic[i]
        print(ans)
        return ans


a = Solution().romanToInt(s="MMMXLV")
