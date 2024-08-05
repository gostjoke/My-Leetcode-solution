## 08/04/2024
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        Sum_Gas, total_Gas, j = 0, 0, 0
        for i in range(len(gas)):
            Sum_Gas += gas[i] - cost[i]
            total_Gas += gas[i] - cost[i]
            if Sum_Gas < 0:
                Sum_Gas = 0
                j = i+ 1
        if total_Gas < 0:
            return -1
        return j
