class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for index, point in enumerate(points):
            value = (point[0])**2+(point[1])**2
            heapq.heappush(heap,(-value,index,point))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[2])

        return result


        
