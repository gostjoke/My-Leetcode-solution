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
