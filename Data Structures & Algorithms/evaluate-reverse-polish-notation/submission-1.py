class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in "+-*/":
                stk.append(int(i))
            else:
                if i == "+":
                    res = stk[-2]+stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(res)
                if i == "-":
                    res = stk[-2]-stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(res)
                if i == "*":
                    res = stk[-2]*stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(res)
                if i == "/":
                    res = int(stk[-2]/stk[-1])
                    stk.pop()
                    stk.pop()
                    stk.append(res)
        return stk.pop()