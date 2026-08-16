class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res=res+",-"+i
        return res

    def decode(self, s: str) -> List[str]:
        res2=s.split(",-")
        return res2[1:]