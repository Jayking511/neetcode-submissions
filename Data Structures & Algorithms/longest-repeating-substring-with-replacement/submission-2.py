class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}
        for r in range(len(s)):
            print(l, r, s[l:r-l+1])
            count[s[r]] = count.get(s[r], 0) + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res