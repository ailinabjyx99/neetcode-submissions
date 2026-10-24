class MedianFinder:

    def __init__(self):
        self.small = [] #right part
        self.large = [] #left part

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large,-num)
        heapq.heappush(self.small,-heapq.heappop(self.large))
        if len(self.small)>len(self.large):
            heapq.heappush(self.large,-heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small)<len(self.large):
            return -self.large[0]
        else:
            return (self.small[0]-self.large[0])/2
        