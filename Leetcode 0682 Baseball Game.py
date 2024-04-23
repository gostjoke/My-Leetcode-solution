"04/23/2023"
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        count = 0
        for i in operations:
            if i == "C":
                ans.pop()
                count -= 1
            elif i == "D":
                ans.append(int(ans[count-1]*2))
                count+=1
            elif i == "+":
                ans.append(int(ans[count-1]) + int(ans[count-2]))
                count +=1 
            else:
                ans.append(int(i))
                count += 1

        return sum(ans)
