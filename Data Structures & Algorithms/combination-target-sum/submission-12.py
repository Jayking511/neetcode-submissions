class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        curr = []
        res = []
        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i, total+nums[i])
            curr.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res