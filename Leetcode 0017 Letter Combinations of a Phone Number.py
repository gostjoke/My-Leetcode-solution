## 2025/07/03
## backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
        }
        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return 
            for letter in dic[digits[idx]]:
                backtrack(idx+1, comb+letter)
        res =[]
        backtrack(0,"")
        return res
## easy way
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        if l == 0:
            return []
        ans = []
        dic = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
        }
        if l == 1:
            return [i for i in dic[digits]]

        elif l == 2:
            for b in dic[digits[1]]:
                for a in dic[digits[0]]:
                    ans.append(f"{a}{b}")
            return ans
        elif l == 3:
            for c in dic[digits[2]]:
                for b in dic[digits[1]]:
                    for a in dic[digits[0]]:
                        ans.append(f"{a}{b}{c}")
            return ans
        elif l == 4:
            for d in dic[digits[3]]:
                for c in dic[digits[2]]:
                    for b in dic[digits[1]]:
                        for a in dic[digits[0]]:
                            ans.append(f"{a}{b}{c}{d}")
            return ans
