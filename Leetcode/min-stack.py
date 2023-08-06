
import heapq
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:

    def __init__(self):
        self.smalls = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smalls:
            self.smalls.append(val)
        elif val <= self.smalls[-1]:
            self.smalls.append(val)
    

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.smalls.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smalls[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
m.pop()
print(m.getMin())