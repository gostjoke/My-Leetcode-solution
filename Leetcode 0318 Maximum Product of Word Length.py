"""
07/31/2023
"""
class Solution:
    def str_dis(self, str1, str2):
        set1 = set(str1)
        set2 = set(str2)

        # 判断两个集合是否有交集
        if set1.intersection(set2):
            return True
        else:
            return False

    def maxProduct(self, words: List[str]) -> int:
        max_no = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.str_dis(words[i], words[j]) is False:
                    max_no = max(max_no, len(words[i])*len(words[j]))  

        return max_no
