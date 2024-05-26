# 05/26/2024
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            prev = 96
            for j in range(len(strs)):
                n = ord(strs[j][i])
                if n >= prev:
                    prev = n
                else:
                    count += 1
                    break
        return count
            
                
