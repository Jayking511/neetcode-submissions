class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c not in d:
                stk.append(c)
            else:
                if stk and d[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True