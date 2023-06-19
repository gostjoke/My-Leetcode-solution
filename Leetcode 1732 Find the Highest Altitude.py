class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        if len(gain) == 1:
            if gain[0] > 0:
                return gain[0]
            else:
                return 0

        alt =[0,gain[0]]
        tmp = gain[0]
        for i in gain[1:]:
            alt.append(i+tmp)
            tmp = i+tmp
        return max(alt)
