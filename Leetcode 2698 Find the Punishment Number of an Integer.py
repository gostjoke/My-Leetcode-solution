## 20250623
class Solution:
    def partition(self, num:str, target):
        if not num and target == 0:
            return True
        if target < 0: return False
        for i in range(len(num)):
            l = num[:i+1]
            r = num[i+1:]
            l_num = int(l)
            if self.partition(r, target - l_num):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for cur_num in range(1, n+1):
            square_num = cur_num*cur_num

            if self.partition(str(square_num), cur_num):
                ans += square_num

        return ans
