class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        for r in range(k, len(nums)+1):
            res.append(max(nums[l:r]))
            l += 1
        return res