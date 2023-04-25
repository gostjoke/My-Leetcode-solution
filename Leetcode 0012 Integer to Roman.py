class Solution:
    def intToRoman(self, num: int) -> str:
        li=len(str(num))-1
        dic = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"}
        
        ans = ""
        for ind, i in enumerate(str(num)):
            i = int(i)
            if i == 4 or i == 5 or i == 9:
                ans += dic[(i*(10**(li-ind)))]
            elif i > 5 and i < 9:
                tmp = i - 5
                ans += dic[5*(10**(li-ind))] + tmp*(dic[10**(li-ind)]) 
            else:
                ans += (i*(dic[10**(li-ind)]))

        return ans

print(Solution().intToRoman(num = 60))