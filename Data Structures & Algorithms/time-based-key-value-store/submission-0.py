class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        left = 0
        right = len(arr)-1
        res = ""

        while left<=right:
            mid = (left+right)//2
            if arr[mid][1]<=timestamp:
                res = arr[mid][0]
                left = mid+1
            else:
                right = mid-1

        return res
        

        
