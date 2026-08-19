class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            n1 = heapq.heappop(maxHeap)
            n2 = heapq.heappop(maxHeap)
            if n1 == n2:
                continue
            else:
                heapq.heappush(maxHeap, -(abs(n1-n2)))
        if len(maxHeap) == 0:
            return 0
        return -(maxHeap[0])