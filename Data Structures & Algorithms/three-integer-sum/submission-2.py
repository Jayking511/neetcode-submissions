class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            for j in range(l, r):
                if l == r:
                    continue
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    tr = [nums[i], nums[l], nums[r]]
                    tr.sort()
                    if tr not in res:
                        res.append(tr)
                    r -= 1
        return res