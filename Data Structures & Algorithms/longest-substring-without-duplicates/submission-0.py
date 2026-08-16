class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] not in s[l:r]:
                r += 1
            else:
                l = l + s[l:r].index(s[i])+1
                r += 1
            max_len = max(max_len, r-l)
            print(i, s[i], l, r, s[l:r], max_len)
        return max_len