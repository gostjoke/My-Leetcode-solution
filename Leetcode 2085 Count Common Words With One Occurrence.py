# 08/09/2024
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a, b = Counter(words1), Counter(words2)
        a = [index for index, i in a.items() if i < 2]
        b = [index for index, i in b.items() if i < 2]   
        return len(set(a) & set(b))
