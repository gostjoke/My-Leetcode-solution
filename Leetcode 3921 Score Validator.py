# 2026/07/31
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        counter = 0
        score = 0
        for i in events:
            if counter == 10:
                break
            if i == "W":
                counter += 1
            elif i in ["WD", "NB"]:
                score += 1
            elif i in ["1","2","3","4","5","6"]:
                score += int(i)
        return [score, counter]
                
        
