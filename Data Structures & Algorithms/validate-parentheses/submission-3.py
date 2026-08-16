class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {"}": "{", ")": "(", "]": "["}
        if s == "":
            return True
        if s[0] not in "{[(":
            return False
        for c in s:
            if c not in d:
                stk.append(c)
            else:
                if stk:
                    tmp = stk.pop()
                    if d[c] == tmp:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stk):
            return False
        return True