# 08/05/2024
class Solution:
    def __init__(self) -> None:
        pass

    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, res, [])
        return res
    def dfs(self, s:str, res:list, path:list):
        print(s, " ", res, " ", path)
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(1, 4):
            
            if i > len(s):
                continue
            if s[:i] == str(int(s[:i])) and int(s[:i]) <=255:
                self.dfs(s[i:], res, path+[s[:i]])

a = Solution().restoreIpAddresses(s="25525511135")
print(a)
