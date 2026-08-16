class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        times = []  # [pos, time]
        stk = []
        for i in range(len(position)):
            times.append([position[i], (target - position[i])/speed[i]])
        times.sort()
        for i in times[::-1]:
            if stk == []:
                stk.append(i[1])
                continue
            if stk[0] >= i[1]:
                stk.append(i[1])
            else:
                stk = [i[1]]
                res += 1
        res += 1
        return res