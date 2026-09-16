class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        position = 0
        def dfs(position):
            if position >= n:
                return position == n
            if position in cache:
                return cache[position]
            cache[position] = dfs(position+1) + dfs(position+2)
            return cache[position]
        return dfs(0)