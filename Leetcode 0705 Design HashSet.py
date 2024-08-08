# 08/08/2024

class MyHashSet:

    def __init__(self):
        self.myHasSet = defaultdict(int)

    def add(self, key: int) -> None:
        self.myHasSet[key] = True

    def remove(self, key: int) -> None:
        self.myHasSet[key] = False

    def contains(self, key: int) -> bool:
        return self.myHasSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
