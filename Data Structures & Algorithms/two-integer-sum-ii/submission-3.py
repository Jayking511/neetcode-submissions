class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = [0, len(numbers)-1]
        while True:
            if numbers[l[0]]+numbers[l[1]] > target:
                l[1] -= 1
                continue
            if numbers[l[0]]+numbers[l[1]] < target:
                l[0] += 1
                continue
            else:
                l[0] += 1
                l[1] += 1
                return l