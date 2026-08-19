class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            n1 = heapq.heappop(maxHeap)
            n2 = heapq.heappop(maxHeap)
            if n2 > n1:
                heapq.heappush(maxHeap, n1-n2)
        maxHeap.append(0)
        return abs(maxHeap[0])