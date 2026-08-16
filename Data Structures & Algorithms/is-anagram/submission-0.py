class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s2 = list(t)
        s1.sort()
        s2.sort()
        if s1 == s2:
            return True
        else:
            return False