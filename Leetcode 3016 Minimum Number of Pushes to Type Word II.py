## 2026/07/30

class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = Counter(word)
        freq = sorted(dic.values(), reverse = True)
        
        count = 0
        for index, q in enumerate(freq):
            count += q * math.ceil((index+1)/8)

        return count

