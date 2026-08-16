class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []  # [temp, ind]
        res = [0]*len(temperatures)
        for i, val in enumerate(temperatures):
            print(i, val)
            if not stk:
                stk.append([val, i])
                continue
            for j in stk[::-1]:
                if val > j[0]:
                    res[j[1]] = i - j[1]
                    stk.pop()
            stk.append([val, i])
            print(stk, res, "\n")
        return res