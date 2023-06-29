'''
06/29/2023
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(pattern) != len(s_list):
            return False
        if len(set(pattern)) != len(set(s_list)): # ['dog', 'cat'], patter = 'aa'
            return False

        dic ={}
        for i in range(len(s_list)):
            if s_list[i] not in dic:
                dic[s_list[i]] = pattern[i]
            elif dic[s_list[i]] != pattern[i]:
                return False
        
        return True
