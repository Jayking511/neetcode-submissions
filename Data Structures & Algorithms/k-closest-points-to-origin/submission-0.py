class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []
        for i in points:
            dist = (0 - i[0])**2 + (0 - i[1])**2
            heapq.heappush(minHeap, [dist, i])
        for i in range(k):
            l = heapq.heappop(minHeap)
            res.append(l[1])
        return res