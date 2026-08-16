class TimeMap:

    def __init__(self):
        self.kvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvs:
            self.kvs[key].append([timestamp, value])
        else:
            self.kvs[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs:
            return ""
        val_list = self.kvs[key]
        l = 0
        r = len(val_list)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if val_list[mid][0] <= timestamp:
                res = val_list[mid][1]
                l = mid+1
            else:
                r = mid-1
        return res