class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()

        def check(p,q):
            area = 1
            if (p,q) in seen:
                return 0
            seen.add((p,q))
            if p < len(grid)-1 and grid[p+1][q] == 1:
                area += check(p+1, q)
            if q < len(grid[0])-1 and grid[p][q+1] == 1:
                area += check(p, q+1)
            if p > 0 and grid[p-1][q] == 1:
                area += check(p-1, q)
            if q > 0 and grid[p][q-1] == 1:
                area += check(p, q-1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue
                if grid[i][j] == 1:
                    area = check(i,j)
                    res = max(res, area)
        return res