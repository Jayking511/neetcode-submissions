class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []  # [temp, ind]
        res = [0]*len(temperatures)
        stk = []  # [temp, ind]
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stackT, stackInd = stk.pop()
                res[stackInd] = i - stackInd
            stk.append([t, i])
        return res