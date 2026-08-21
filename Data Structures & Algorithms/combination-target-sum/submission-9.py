class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        res = []
        total = 0
        subset = []
        def dfs(i):
            nonlocal total

            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            subset.append(nums[i])
            total += nums[i]
            dfs(i)

            total -= nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
