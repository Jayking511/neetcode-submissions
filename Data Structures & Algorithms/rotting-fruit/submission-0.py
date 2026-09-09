class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        time = 0
        fresh = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    r1 = r + d[0]
                    c1 = c + d[1]
                    if (r1 < 0 or r1 >= ROWS or
                        c1 < 0 or c1 >= COLS or
                        grid[r1][c1] != 1):
                        continue
                    grid[r1][c1] = 2
                    q.append([r1, c1])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1