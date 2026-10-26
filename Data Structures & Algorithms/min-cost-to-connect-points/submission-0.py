class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0,0)]
        visited = set()
        total = 0

        while len(visited)<n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total+=cost
            for j in range(n):
                if j not in visited:
                    d = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    heapq.heappush(heap,(d,j))
        return total