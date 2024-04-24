# 04/23/2024
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        
        for ind, i in enumerate(mountain):
            if ind != 0 and ind != (len(mountain)-1):
                if i > mountain[ind-1] and i > mountain[ind+1]:
                    ans.append(ind)
        
        return ans

