class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        for i in range(len(s2)-l1+1):
            if sorted(s2[i:i+l1]) == sorted(s1):
                return True
        return False