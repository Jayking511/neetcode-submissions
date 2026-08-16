class MinStack:

    def __init__(self):
        self.stk = []
        self.mn = None
        return None

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(val)
            self.mn = val
        else:
            self.stk.append(val)
            self.mn = min(val, self.mn)

    def pop(self) -> None:
        n = self.stk[-1]
        self.stk.pop()
        if self.stk:
            self.mn = min(self.stk)
        else:
            mn = None

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mn