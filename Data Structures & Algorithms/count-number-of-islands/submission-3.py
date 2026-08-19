class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0

        def check_around(p,q):
            if (p,q) in seen:
                return
            seen.add((p,q))
            if p < len(grid)-1 and grid[p+1][q] == "1":
                check_around(p+1, q)
            if p >=1 and grid[p-1][q] == "1":
                check_around(p-1, q)
            if q < len(grid[0])-1 and grid[p][q+1] == "1":
                check_around(p, q+1)
            if q >= 1 and grid[p][q-1] == "1":
                check_around(p, q-1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    check_around(i, j)
        return count