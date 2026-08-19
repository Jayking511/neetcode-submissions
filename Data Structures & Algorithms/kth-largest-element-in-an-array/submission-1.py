class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = None
        heapq.heapify(nums)
        l = len(nums)
        for i in range(l-k+1):
            res = heapq.heappop(nums)
        return res