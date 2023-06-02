"""
6/1/2023 7:30pm
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic1 = {}
        for j in magazine:
            try:
                dic1[j] += 1
            except:
                dic1[j] = 1 


        for i in ransomNote:
            value = dic1.get(i)
            if not value:
                return False
            else:
                dic1[i] -= 1
        
        return True
