# "04/23/2024"
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i.startswith(".."):
                count -=1
                if count < 0:
                    count = 0
            elif i.startswith("."):
                pass
            else:
                count += 1
        return count 
