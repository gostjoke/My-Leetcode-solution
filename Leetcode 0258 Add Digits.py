'''
06/27/2023
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            tmp = 0
            for i in str(num):
                tmp += int(i)
            num = tmp
        return num

"""
07/14/2023
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            ans = 0
            while num:
                ans += (num%10)
                num = num//10
                print(num)

            num = ans
        return num
