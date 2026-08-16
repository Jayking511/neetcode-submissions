class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if i!=j:
                    val*=nums[j]
            res.append(val)
        return res