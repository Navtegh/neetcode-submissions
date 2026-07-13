class MinStack:

    def __init__(self):
        self.x=[]
        self.minx=[]
    def push(self, val: int) -> None:
        self.x.append(val)
        val = min(val, self.minx[-1] if self.minx else val)
        self.minx.append(val)

    def pop(self) -> None:
        self.x.pop()
        self.minx.pop()
    def top(self) -> int:
        return self.x[-1]
    def getMin(self) -> int:
        return self.minx[-1]
