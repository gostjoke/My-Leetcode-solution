#2026/07/23

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = []
        tmp = ""
        for i in paragraph+" ":
            if i in ["!","?", "'", ",", ";", ".", " "]:
                if tmp.isalpha():
                    para.append(tmp)
                tmp = ''
            else:
                tmp += i

        words_dic = {}
        count = 0
        ans = ''
        for s in para:
            s = s.lower()
            if s not in banned:
                if s in words_dic:
                    words_dic[s] += 1
                else:
                    words_dic[s] = 1
                if words_dic[s] > count:
                    count = words_dic[s]
                    ans=s
        return ans
                
