class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mink = r
        while l <= r:
            k = (l+r)//2
            total_hours = 0
            for i in piles:
                if i % k:
                    total_hours = total_hours + (i//k) + 1
                else:
                    total_hours = total_hours + (i//k)
            if total_hours > h:
                l = k + 1
            else:
                r = k - 1
                mink = min(mink, k)
        return mink