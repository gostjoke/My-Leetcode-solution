# '05/17/2024'
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return (' ').join(s.split(' ')[:k])
