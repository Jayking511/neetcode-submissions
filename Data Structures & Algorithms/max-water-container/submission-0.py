class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                vol = min(heights[i], heights[j])*(j-i)
                if vol > maxvol:
                    maxvol = vol
        return maxvol