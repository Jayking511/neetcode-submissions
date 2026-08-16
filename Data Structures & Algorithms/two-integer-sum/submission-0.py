class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[0]*2
        for i in range(len(nums)):
            for j in range (1, len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    result[0] = i
                    result[1] = j
                    return result