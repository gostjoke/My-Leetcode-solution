# 08092024
class Solution:
    def findComplement(self, num: int) -> int:
        a = ""
        for i in bin(num)[2:]:
            if i == "1":
                a+="0"
            else:
                a+="1"
        return int(a, 2)
