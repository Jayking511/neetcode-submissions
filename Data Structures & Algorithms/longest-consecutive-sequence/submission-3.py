class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num-1 not in numset:
                len = 0
                while (num+len) in numset:
                    len += 1
                    longest = max(len, longest)
        return longest