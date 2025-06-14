# 20250613
# O(1) version
class RandomizedSet:

    def __init__(self):
        self.val_ind = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.val_ind[val] = len(self.values)
        self.values.append(val)        
        return True
    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        """
        {
            3:0
            4:1
            9:2
            7:3
            5:4
         }
        [3,4,9,7,5] remove 9
        """
        idx = self.val_ind[val] # idx-> 3
        last_val = self.values[-1] # last_vale -> 5
        self.values[idx] = last_val # 9 replace by 5 [3,4,5,7,5]
        self.val_ind[last_val] = idx
        self.values.pop()
        del self.val_ind[val]   
        return True    

    def getRandom(self) -> int:
        return random.choice(self.values)
            
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# O(n) version due to random.choice(list(self.a))
class RandomizedSet:

    def __init__(self):
        self.a = set()

    def insert(self, val: int) -> bool:
        if val not in self.a:
            self.a.add(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.a:
            self.a.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.a))
