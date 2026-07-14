from collections import deque
class MinStack:

    def __init__(self):
        self.cont = deque()

    def push(self, val: int) -> None:
        self.cont.append(val)

    def pop(self) -> None:
        return self.cont.pop()
        

    def top(self) -> int:
        return self.cont[-1]

    def getMin(self) -> int:
        mn = self.cont[0]
        for i in self.cont:
            if mn > i:
                mn = i
        return mn
