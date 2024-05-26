# 0526/2024
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return (" ").join([i.lower().capitalize() if len(i) > 2 else i.lower() for i in title.split(" ")])
