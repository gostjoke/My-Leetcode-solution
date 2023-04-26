"""
4/26/2023
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # ord("0")= 48, ord("1") = 49, # ord("9") =57
        li1 = len(num1)-1 
        li2 = len(num2)-1
        counter = 0
        for ind, i in enumerate(num1):
            for ind2, j in enumerate(num2):
                counter += (ord(i)-48)*(10**(li1-ind))*(ord(j)-48)*(10**(li2-ind2))
        return str(counter)
