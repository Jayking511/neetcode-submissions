class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [[-1]*2 for _ in range(len(nums))]
        if len(nums) <= 2:
            return max(nums)
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            if cache[i][flag] != -1:
                return cache[i][flag]
            cache[i][flag] = max(nums[i]+dfs(i+2, flag), dfs(i+1, flag))
            return cache[i][flag]
        return max(dfs(0, True), dfs(1, False))