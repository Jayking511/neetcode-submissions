class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        minstr = ""
        dt = {}
        ds = {}
        for i in t:
            dt[i] = dt.get(i, 0) + 1

        l = 0
        r = 0
        ds = {s[0]: 1}
        while r < len(s):
            if len(ds) < len(dt) or len(s) < len(t):
                r += 1
                if r == len(s):
                    break
                ds[s[r]] = ds.get(s[r], 0) + 1
                continue
            lessthant = False
            for i in t:
                if dt[i] > ds.get(i, 0):
                    lessthant = True
                    break
            if lessthant == True:
                r += 1
                if r == len(s):
                    break
                ds[s[r]] = ds.get(s[r], 0) + 1
                continue
            if minstr == "" or len(minstr) > (r-l+1):
                minstr = s[l:r+1]
            ds[s[l]] -= 1
            l += 1
        return minstr