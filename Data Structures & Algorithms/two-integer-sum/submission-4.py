class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i, n in enumerate(nums):
            indices.append([n, i])
        indices.sort()
        l, r = 0, len(nums)-1
        while r > l:
            if indices[l][0] + indices[r][0] == target:
                return [
                    min(indices[l][1], indices[r][1]),
                    max(indices[l][1], indices[r][1])
                ]
            elif indices[l][0] + indices[r][0] < target:
                l+=1
            else:
                r-=1
        return []