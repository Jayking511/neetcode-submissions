class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        res = []
        for i in range(len(strs)):
            if i not in check:
                check[i] = strs[i]
                ana = [strs[i]]
                for j in range(i+1, len(strs)):
                    if j not in check and sorted(strs[i]) == sorted(strs[j]):
                        ana.append(strs[j])
                        check[j] = strs[j]
                res.append(ana)
        return res