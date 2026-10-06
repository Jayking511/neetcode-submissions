class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
                continue
            product_all *= i
        if zero_cnt > 1:
            return [0]*len(nums)
        res = [0]*len(nums)
        for i, n in enumerate(nums):
            if zero_cnt == 1:
                if n == 0:
                    res[i] = product_all
                    return res
            else:
                res[i] = (product_all // n)
        return res