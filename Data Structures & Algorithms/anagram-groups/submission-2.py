class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in d:
                d[key].append(i)
            else:
                d[key] = [i]
        finallist = []
        for i, val in d.items():
            finallist.append(val)
        return finallist