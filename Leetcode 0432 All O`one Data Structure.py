### 2025/12/15
### must improve
class AllOne:

    def __init__(self):
        self._dict = {}

    def inc(self, key: str) -> None:
        if key not in self._dict:
            self._dict[key] = 1
        else:
            self._dict[key] += 1

    def dec(self, key: str) -> None:
        self._dict[key] -= 1
        if self._dict[key] == 0:
            del self._dict[key]

    def getMaxKey(self) -> str:
        if not self._dict:
            return ""
        max_key = ""
        max_c = 0
        for key, c in self._dict.items():
            if c > max_c:
                max_c = c
                max_key = key
        return max_key

    def getMinKey(self) -> str:
        if not self._dict:
            return ""
        min_key = ""
        min_c = float('inf')
        for key, c in self._dict.items():
            if c < min_c:
                min_c = c
                min_key = key
        return min_key    


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
