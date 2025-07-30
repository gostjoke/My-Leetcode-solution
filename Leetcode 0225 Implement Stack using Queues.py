# 20250729
class MyStack:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l = [x] + self.l

    def pop(self) -> int:
        t = self.l[0] 
        self.l = self.l[1:]
        return t

    def top(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        return len(self.l) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
