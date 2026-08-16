class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, val in enumerate(temperatures):
            cnt = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > val:
                    cnt = j-i
                    break
            res.append(cnt)
        return res