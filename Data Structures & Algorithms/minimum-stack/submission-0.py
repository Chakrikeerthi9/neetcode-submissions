from collections import deque
class MinStack:

    def __init__(self):
        self.container = deque()

    def push(self, val: int) -> None:
        self.container.append(val)

    def pop(self) -> None:
        return self.container.pop()

    def top(self) -> int:
        if len(self.container) != 0:
            return self.container[-1]

    def getMin(self) -> int:
        mn = self.container[0]
        for i in self.container:
            if i < mn:
                mn = i
        return mn
