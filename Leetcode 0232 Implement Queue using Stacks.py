# 20250729

class MyQueue:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l += [x]

    def pop(self) -> int:
        t = self.l[0]
        self.l = self.l[1:]
        return t

    def peek(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        return len(self.l) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
