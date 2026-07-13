class MinStack:

    def __init__(self):
        self.x=[]

    def push(self, val: int) -> None:
        self.x.append(val)

    def pop(self) -> None:
        self.x.pop()
        print(self.x)
    def top(self) -> int:
        return self.x[-1]

    def getMin(self) -> int:
        return min(self.x)
