class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        rem = l % 2
        quo = l//2
        if rem == 0:
            return (nums1[quo]+nums1[quo-1])/2
        else:
            return nums1[quo]