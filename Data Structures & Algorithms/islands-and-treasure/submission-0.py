class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r<0 or r == rows or c<0 or c == cols or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1