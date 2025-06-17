# 20250616

class MinStack:

    def __init__(self):
        self.ans = []
        self.min_stack =[] 

    def push(self, val: int) -> None:
        self.ans.append(val)
        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self.ans.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
