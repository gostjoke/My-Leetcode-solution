# 20250807
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        elif len(timeSeries) == 1:
            return duration
        # we add last duration in here
        ans = duration
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] < duration:
                ans += timeSeries[i+1] - timeSeries[i]
            else:
                ans += duration

        return ans
