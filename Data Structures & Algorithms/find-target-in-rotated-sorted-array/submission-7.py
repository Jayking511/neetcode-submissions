class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while r >= l:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target == nums[0]:
                return 0
            if target > nums[0] and target < nums[mid]:
                r = mid-1
                continue
            elif target > nums[0] and target > nums[mid]:
                if nums[mid] < nums[0]:
                    r = mid-1
                else:
                    l = mid+1
                continue
            elif target < nums[0] and target < nums[mid]:
                if nums[mid] < nums[0]:
                    r = mid-1
                else:
                    l = mid+1
                continue
            elif target < nums[0] and target > nums[mid]:
                l = mid+1
                continue
        return -1