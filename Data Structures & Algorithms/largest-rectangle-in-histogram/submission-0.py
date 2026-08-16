class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightset = set(heights)
        maxarea = 0
        for i in heightset:
            maxiarea = 0
            iarea = 0
            for j in range(len(heights)):
                if heights[j] >= i:
                    iarea += i
                else:
                    maxiarea = max(maxiarea, iarea)
                    iarea = 0
                if j == len(heights)-1:
                    maxiarea = max(maxiarea, iarea)
            maxarea = max(maxarea, maxiarea)
        return maxarea