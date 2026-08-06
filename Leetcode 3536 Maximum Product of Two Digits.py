# 2026/08/06
class Solution:
    def maxProduct(self, n: int) -> int:
        dict_n = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0,
            0:0,
        }
        for i in str(n):
            dict_n[int(i)] += 1
        dict_n = {k: dict_n[k] for k in sorted(dict_n, reverse=1) if dict_n[k] != 0}
        ans = 1
        muli = 0 # max 2
        for key, item in dict_n.items():
            if item > 1 and muli == 0:
                return key*key
            else:
                ans *= key
                muli += 1
            if muli == 2:
                break
        return ans

        
