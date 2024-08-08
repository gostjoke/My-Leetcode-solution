# 08082024
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        score_2 = sorted(score, reverse=True)
        for index, i in enumerate(score_2):
            if index == 0:
                dic[f"{i}"] = "Gold Medal"
            elif index == 1:
                dic[f"{i}"] = "Silver Medal"
            elif index == 2:
                dic[f"{i}"] = "Bronze Medal"
            else:
                dic[f"{i}"]=str(index+1)
        score= [dic[str(i)] for i in score]
        return score
