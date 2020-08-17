# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minList = []
        self.min = float("inf")

    def push(self, x: int) -> None:
        if not self.stack:
            self.minList.append(x)
            self.min = x
        else:
            if x < self.min:
                self.minList.append(x)
                self.min = x
            else:
                self.minList.append(self.min)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minList.pop()
        if self.minList:
            self.min = self.minList[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minList:
            return self.minList[-1]

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)

print(obj.top())
obj.pop()

print(obj.stack)
print(obj.minList)

print(obj.getMin())
obj.pop()
print(obj.getMin())
print(obj.getMin())
obj.pop()
