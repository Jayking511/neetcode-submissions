class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
                    dic[num] = dic.get(num, 0) + 1

        arr = []
        for num, cnt in dic.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res