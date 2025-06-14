# 20250614

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for index , i in enumerate(s):
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for index, i in enumerate(s):
            if dic[i] == 1:
                return index
        return -1
