# 2025/12/15
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            for j in range(60):
                if i.bit_count() + j.bit_count() == turnedOn:
                    ans.append(f"{i}:{j:02d}")
        return ans
