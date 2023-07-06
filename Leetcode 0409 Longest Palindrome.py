'''
07/06/2023
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        for i in s:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        
        check_odd = False
        ans = 0
        for j, item in dic.items():
            if item % 2 == 1:  # becasue Odd only can use 1 to be center 
                check_odd = True
            if item % 2 == 1 and item > 1: # if have more than one odd just add its even
                ans += (item-1)
            elif item % 2 == 0:
                ans += item
        
        if check_odd:
            return ans + 1
        else:
            return ans
