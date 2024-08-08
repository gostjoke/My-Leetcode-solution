## 08/08/2024

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [index for index, items in Counter((s1 + " " + s2).split(" ")).items() if items==1 ]
        # my_counter = Counter((s1 + " " + s2).split(" "))
        # ans = []
        # for index, items in my_counter.items():
        #     if items == 1:
        #         ans.append(index)
        # return ans
