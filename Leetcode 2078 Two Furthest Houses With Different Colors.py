## 06/15/2024
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # both side check
        n = len(colors)
        if n <= 1:
            return 0
        elif n <=2:
            return 1
        max_range=0
        for i in range(n):
            if colors[i] != colors[0]:
                max_range = max(max_range, i)
            if colors[i] != colors[-1]:
                max_range = max(max_range, n-1-i)

        return max_range

        
